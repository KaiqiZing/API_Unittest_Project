# coding=utf-8
import requests
import json
"""
request的使用规则
"""
class RunMain:
    def __init__(self,url,method,data=None):
        self.res = self.run_main(url, method, data)

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None):

        res = None
        if method == "GET":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res

if __name__ == '__main__':
    url = 'http://sellshop.5istudy.online/sell/buyer/product/list'
    run = RunMain(url,'GET')
    print(run.res)