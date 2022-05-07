#coding=utf-8
# import HTMLTestRunner
import unittest
import json
from demo import RunMain
from mock import mock
from mock_demo import mock_test
class TestMethod(unittest.TestCase):

    # 测试前置和后置
    def setUp(self):
        print("这是前置执行")

    def test_01(self):
        url = 'http://sellshop.5istudy.online/sell/buyer/product/list'  # 正确的地址

        # url = 'http://sellshop.5istudy.online/sell/buyer/product/liszt'  # 错误的地址

        self.run = RunMain(url,"GET")
        res = self.run.run_main(url, "GET")
        print(res)

        # 引入断言做判断
        self.assertNotEqual(res['message'], "No message available", "测试失败")
        print("这是第一个case")


    # @unittest.skip("test_02")  # 指定跳过该用例执行
    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0',
            'errorCode':1008

        }


        # 引入mock，mock基本使用；
        # self.run = RunMain(url,"POST")
        # mock_data = mock.Mock(return_value=data)
        # self.run.run_main = mock_data  # 模拟出来的返回结果
        # res = self.run.run_main(url, "POST", data)

        # 封装mock后的用法：
        self.run = RunMain(url,"POST")
        res = mock_test(self.run.run_main, data, url, "POST", data)

        # 引入断言做判断
        # Python源代码错误，双重否定就是肯定
        self.assertNotEqual(res['errorCode'],1007,"测试失败")
        print(res)
        print("这是第二个case")

if __name__ == '__main__':
    # 第一种执行方式：
    # unittest.main()

    #第二种执行方式---问题执行时不能单独执行
    suite = unittest.TestSuite()
    suite.addTest(TestMethod("test_02"))
    result = unittest.TestResult()
    suite.run(result)