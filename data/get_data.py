# coding=utf-8
#通过组成data_config and OperatonExcel来获取每条case的参数并执行；
import sys
sys.path.append("/Users/mac/PycharmProjects/API_Unittest_Project")
from util.operation_excel import OperationExcel
from data import data_config
from util.operation_json import OperationJson

class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    # 获取某个单元格的数据

    # def process_getcellvalue(self,row, col):
    #     return self.opera_excel.get_cell_value(row, col)
    # # 获取excel行数，就是我们case个数
    # def get_case_lines(self):
    #     return self.opera_excel.get_lines()
    # # 是否执行
    # def get_is_run(self,row):
    #     flag = None
    #     col = int(self.global_test.get_run())
    #     run_model = self.process_getcellvalue(row,col)
    #     if run_model == "yes":
    #         flag = True
    #     else:
    #         flag = False
    #     return flag
    #
    # # 是否携带header
    # def is_header(self,row):
    #     col = int(self.global_test.get_header())
    #     header = self.process_getcellvalue(row,col)
    #     if header != "":
    #         return header
    #     else:
    #         return None
    # # 获取请求方式
    # def get_request_method(self,row):
    #     col = int(self.global_test.get_run_way())
    #     request_method = self.process_getcellvalue(row,col)
    #     return request_method
    # #  获取url
    # def get_request_url(self, row):
    #     col = int(self.global_test.get_url())
    #     url = self.process_getcellvalue(row,col)
    #     return url
    #
    # # 获取请求数据
    # def get_request_data(self,row):
    #     col = int(self.global_test.get_data())
    #     data = self.process_getcellvalue(row,col)
    #     if data == "":
    #         return None
    #     return data
    # # 通过关键字获取数据
    # def get_data_for_json(self,row):
    #     oper_json = OperationJson()
    #     request_data = oper_json.get_json_data(self.get_request_data(row))
    #     return request_data
    # # 获取预期结果
    # def get_except_data(self,row):
    #     col = int(self.global_test.get_except_result())
    #     except_result = self.process_getcellvalue(row,col)
    #     if except_result == "":
    #         return None
    #     return except_result
    # # 获取实际结果
    # def get_actual_result(self,row,value):
    #     col = int(self.global_test.get_actual_result())
    #     self.opera_excel.write_value(row,col,value)  # 获取到写入数据后的值
    #
    # # 获取依赖数据的key
    # def get_depend_key(self,row):
    #     col = int(self.global_test.get_data_spend())
    #     depend_id = self.process_getcellvalue(row,col)
    #     if depend_id == "":
    #         return None
    #     else:
    #         return depend_id
    # # 判断是否有依赖case
    # def is_depend(self,row):
    #     col = int(self.global_test.get_case_depend())
    #     depend_case_id = self.process_getcellvalue(row,col)
    #     if depend_case_id == "":
    #         return None
    #     return depend_case_id
    # # 获取数据依赖字段
    #
    # def get_depend_field(self, row):
    #     col = int(self.global_test.get_field_spend())
    #     data = self.process_getcellvalue(row,col)
    #     if data == "":
    #         return None
    #     else:
    #         return data
    #
    #
    # def wirte_result(self, row, value):
    #     col = int(self.global_test.get_except_result())
    #     self.process_getcellvalue(row,col,value)


# 去获取excel行数,就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()


    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag


    # 是否携带header
    def is_header(self, row):
        col = int(data_config.get_header())
        header = self.opera_excel.get_cell_value(row, col)
        if header != '':
            return header
        else:
            return None


    # 获取请求方式
    def get_request_method(self, row):
        col = int(data_config.get_run_way())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method


    # 获取url
    def get_request_url(self, row):
        col = int(data_config.get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url


    # 获取请求数据
    def get_request_data(self, row):
        col = int(data_config.get_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data


    # 通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_json_data(self.get_request_data(row))
        return request_data


    # 获取预期结果
    def get_expcet_data(self, row):
        col = int(data_config.get_except_result())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect


    # # 通过sql获取预期结果
    # def get_expcet_data_for_mysql(self, row):
    #     op_mysql = OperationMysql()
    #     sql = self.get_expcet_data(row)
    #     res = op_mysql.search_one(sql)
    #     return res.decode('unicode-escape')


    def write_result(self, row, value):
        col = int(data_config.get_except_result())
        self.opera_excel.write_value(row, col, value)


    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = int(data_config.get_case_depend())
        depent_key = self.opera_excel.get_cell_value(row, col)
        if depent_key == "":
            return None
        else:
            return depent_key


    # 判断是否有case依赖
    def is_depend(self, row):
        col = int(data_config.get_case_depend())
        depend_case_id = self.opera_excel.get_cell_value(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id


    # 获取数据依赖字段
    def get_depend_field(self, row):
        col = int(data_config.get_field_spend())
        data = self.opera_excel.get_cell_value(row, col)
        if data == "":
            return None
        else:
            return data
