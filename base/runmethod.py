# coding=utf-8
import json

import requests
class RunMethod:

    # def post_main(self, url,data,header=None):
    #     res = None
    #     if header != None:
    #         res = requests.post(url=url, data=data, headers= header)
    #         print(res)
    #     else:
    #         res = requests.post(url=url, data=data)
    #     return res.json()
    #
    # def get_main(self,url, data, header=None):
    #     res = None
    #     if  header != None:
    #         res = requests.get(url=url, data=data, headers=header, verify=False)
    #     else:
    #         res = requests.get(url=url, data=data, verify=False)
    #     return res.json()
    #
    # def run_main(self,method, url, data=None, header=None):
    #     res = None
    #     if method =="Post":
    #         res = self.post_main(url,data,header)
    #         print("res")
    #     else:
    #         res = self.get_main(url,data,header)
    #     # return json.dumps(res, ensure_ascii=False)
    #     return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)


    def post_main(self, url, data, header=None):
        res = None
        if header != "no":
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()


    def get_main(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()


    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False)
        #  return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)

        # return res