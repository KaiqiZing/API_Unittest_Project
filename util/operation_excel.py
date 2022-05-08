# coding=utf-8
import xlrd
from xlutils.copy import copy

class OperationExcel:

    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = "/Users/mac/PycharmProjects/API_Unittest_Project/dataconfig/case1.xls"
            self.sheet_id = 0
        self.data = self.get_data()



    # 获取sheet 内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self,row,col):
        return self.data.cell_value(row, col)


    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    # 根据caseid找到对应的行内容
    def get_row_data(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)
        return row_data

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        cols_data = self.get_col_data()
        for cols_datas in cols_data:
            if case_id in cols_datas:
                return num
            num += 1



    # 获取行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取列的内容
    def get_col_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols
if __name__ == '__main__':
    opera = OperationExcel()
    print(opera.get_cell_value(1,1))


