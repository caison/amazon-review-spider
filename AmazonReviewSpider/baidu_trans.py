# /usr/bin/env python
# coding=utf8
import hashlib
import random
import urllib

import requests


class BaiduTrans(object):
    def __init__(self):
        self.httpClient = None
        self.base_url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        self.request_session = requests.session()
        self.appId = '20170821000075622'
        self.secretKey = 'eBnL61SbV_jhi9E0cHTS'

    def transEn2Zh(self, text):
        fromLang = 'en'
        toLang = 'zh'
        salt = random.randint(32768, 65536)
        sign = self.appId + text + str(salt) + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        req_url = self.base_url + '?appid=' + self.appId + '&q=' + urllib.parse.quote(
            text) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

        print('url=' + req_url)
        try:
            response = self.request_session.get(req_url).content
            response = response.decode('unicode_escape', 'ignore')
            content = str(response)
            print(content)
            trans_result_list = eval(content).get('trans_result')
            trans_result = trans_result_list[0].get('dst')
            return trans_result
        except Exception as e:
            print(e)

if __name__ == '__main__':
    ret = BaiduTrans().transEn2Zh("hello,word")
    print(ret)
