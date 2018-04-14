from lxml import etree

from AmazonReviewSpider.baidu_trans import BaiduTrans


class HtmlParser(object):
    def __init__(self, base_url):
        self.amazon_base_url = base_url
        self.trans = BaiduTrans()

    # 从主页获取See all 73 positive reviews的url链接
    def parse_main_page_reviews_url(self, content):
        content = str(content)
        html = etree.HTML(content)
        subject = html.xpath('//a[@id="dp-summary-see-all-reviews" and @class="a-link-emphasis"]')
        a_href = subject[0].get('href')

        return self.amazon_base_url + a_href

    def get_next_reviews_url(self, content):
        content = str(content)
        html = etree.HTML(content)
        subject = html.xpath('//li[@class="a-last"]/a')
        # 表示已经没有下一页
        if len(subject) == 0:
            return ""

        a_href = subject[0].get('href')
        return self.amazon_base_url + a_href

    def get_reviews_info(self, content):
        content = str(content)
        content = content.replace("<br>", "")
        content = content.replace("<br />", "")
        html = etree.HTML(content)

        star_list = html.xpath('//a/i[@data-hook="review-star-rating"]/span[@class="a-icon-alt"]/text()')
        title_list = html.xpath('//div[@class="a-row"]/a[@data-hook="review-title"]/text()')

        review_body_list = html.xpath('//div[@class="a-row review-data"]/span['
                                      '@data-hook="review-body"]/text()')

        all_review_list = []
        for index in range(len(star_list)):
            star_num = star_list[index][:1]
            if int(star_num) < 4:
                continue
            all_review_list.append(
                {"star": star_num, "title": title_list[index], "body": review_body_list[index],
                 'trans': self.trans.transEn2Zh(review_body_list[index])})

        return all_review_list


if __name__ == '__main__':
    '''
    downloader = Downloader()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
    }

    url = "https://www.amazon.co.uk/Transmission-Lullabies-Temperature-Monitoring-Discoball%C2%AE/product-reviews/B01HXPQUUI/ref=cm_cr_getr_d_paging_btm_12?ie=UTF8&pageNumber=12&reviewerType=all_reviews"
    # url_final = "https://www.amazon.co.uk/Transmission-Lullabies-Temperature-Monitoring-Discoball%C2%AE/product-reviews/B01HXPQUUI/ref=cm_cr_getr_d_paging_btm_12?ie=UTF8&reviewerType=all_reviews&pageNumber=12";
    content2 = downloader.download(url, retry_count=2, headers=headers).decode('utf8')
    HtmlParser().get_reviews_info(content2)
    '''

    star = '1.0 of 5'
    print(star[:1])
