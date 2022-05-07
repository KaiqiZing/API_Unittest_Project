# coding=utf-8
import json
# 对json文件进行读写操作

class OperationJson:
    def __init__(self):
        self.data = self.read_data()
    def read_data(self,id):
        with open("/Users/mac/PycharmProjects/API_Unittest_Project/dataconfig/user.json") as json_file:
            data = json.load(json_file)
            return data
    def get_json_data(self, id):
        return self.data[id]
if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_json_data("addcart"))