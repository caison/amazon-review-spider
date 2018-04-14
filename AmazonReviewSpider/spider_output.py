# encoding='utf8'
import os
import time
import xlwt


class OutPutUse(object):
    def __init__(self):
        self.wb = xlwt.Workbook(encoding='UTF-8')

    def add_review_info(self, sheet_name, main_url, all_review_info):
        # 新增一个表单
        sh = self.wb.add_sheet(sheet_name)
        sh.write(0, 0, main_url)
        sh.write(1, 0, '评分数')
        sh.write(1, 1, '标题')
        sh.write(1, 2, '内容')
        sh.write(1, 3, '内容翻译')

        for index in range(len(all_review_info)):
            sh.write(index + 2, 0, all_review_info[index].get("star"))
            sh.write(index + 2, 1, all_review_info[index].get("title"))
            sh.write(index + 2, 2, all_review_info[index].get("body"))
            sh.write(index + 2, 3, all_review_info[index].get("trans"))

    def save_review_info(self):
        file_name = "评论数据" + time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        save_dir = '评论数据' + os.path.sep + file_name + ".xls"
        self.wb.save(save_dir)


if __name__ == '__main__':
    pass
