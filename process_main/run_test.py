# coding=utf-8
import sys
sys.path.append("/Users/mac/PycharmProjects/API_Unittest_Project")
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_utils import CommonUtil
from util.operation_json import OperationJson
import dataconfig
from data.dependent_data import Dependent_data
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.comutil = CommonUtil()

    def got_to_run(self):
        res = None
        pass_count = []
        fail_count = []
        row_count = self.data.get_case_lines()
        for i in range(2,5):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                except_data = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = Dependent_data(depend_case)
                    # 读取依赖响应数据
                    depend_reponse_data = self.data.get_depend_key(i)
                    # 获取以来的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_reponse_data
                res = self.run_method.run_main(method, url, request_data, header)
                print(type(res))
                print(type(except_data))
                if self.comutil.is_contain(except_data, res):
                    self.data.write_result(i, "pass")
                else:
                    self.data.write_result(i, "fail")







if __name__ == '__main__':
    run = RunTest()
    print(run.got_to_run())

