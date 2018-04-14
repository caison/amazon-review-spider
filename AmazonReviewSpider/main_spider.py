# encoding='utf8'
from AmazonReviewSpider.html_downloader import Downloader
from AmazonReviewSpider.html_parser import HtmlParser
from AmazonReviewSpider.spider_output import OutPutUse
from AmazonReviewSpider.url_manager import UrlManager

'''
在尝试重新打包并且使用--hidden-import queue 后，程序能够正常运行。
pyinstaller -F --hidden-import=queue main_spider.py  
'''


class Scheduler(object):
    def __init__(self):
        self.url_manager = UrlManager()
        self.downloader = Downloader()
        self.parser = HtmlParser(self.url_manager.get_amazon_base_url())
        self.output = OutPutUse()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
        }

    def get_all_review_url(self, main_page_reviews_url):
        review_content = self.downloader.download(main_page_reviews_url, retry_count=2, headers=self.headers)
        reviews_url_list = [main_page_reviews_url]

        next_reviews_url = self.parser.get_next_reviews_url(review_content)
        while next_reviews_url != "":
            reviews_url_list.append(next_reviews_url)
            review_content = self.downloader.download(next_reviews_url, retry_count=2, headers=self.headers)
            next_reviews_url = self.parser.get_next_reviews_url(review_content)
        return reviews_url_list

    def run(self):
        main_url_list = self.url_manager.get_all_main_url_from_file()

        for index in range(len(main_url_list)):
            main_url = main_url_list[index]
            try:
                self.run_a_main_url(index, main_url)
            except BaseException as e:
                print("商品抓取评论失败，地址:" + main_url + e)
        self.output.save_review_info()

    def run_a_main_url(self, index, main_url):
        content = self.downloader.download(main_url, retry_count=2, headers=self.headers)
        main_page_reviews_url = self.parser.parse_main_page_reviews_url(content)
        print("Scheduler.run开始下载商品评论，index=" + str(index))
        all_review_url = self.get_all_review_url(main_page_reviews_url)
        print("Scheduler.run商品评论下载完毕，index=" + str(index))
        review_info_list = []
        for url in all_review_url:
            content = self.downloader.download(url, retry_count=2, headers=self.headers)
            review_info_list.extend(self.parser.get_reviews_info(content))
        self.output.add_review_info("NO_" + str(index + 1), main_url, review_info_list)


if __name__ == '__main__':
    schedule = Scheduler()
    schedule.run()
    # schedule.run()
