import os


class UrlManager(object):
    def __init__(self):
        pass

    def get_all_main_url_from_file(self):
        input_dir = "输入信息" + os.path.sep + "商品地址文件.txt"


        try:
            file_object = open(input_dir)
        except IOError:
            print("读取文件识别，找不到如下文件：商品地址文件.txt")
            return

        try:
            all_main_url_list = file_object.readlines()
        finally:
            file_object.close()
        if len(all_main_url_list) == 0:
            raise Exception("获取亚马逊基础地址失败，商品地址文件为空")

        all_main_url_list = list(map(lambda x: x.replace("\n", ""), all_main_url_list))
        return list(filter(lambda x: len(x) > 10, all_main_url_list))

    def get_amazon_base_url(self):
        all_main_url_list = self.get_all_main_url_from_file()
        one_url = all_main_url_list[0]
        if "https://www.amazon.ca" in one_url:
            return "https://www.amazon.ca"
        if "https://www.amazon.co.uk" in one_url:
            return "https://www.amazon.co.uk"
        raise Exception("获取亚马逊地址失败")


if __name__ == '__main__':
    list = UrlManager().get_all_main_url_from_file()
    print(list)
