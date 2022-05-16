# coding=utf-8
import json
# 对json文件进行读写操作

class OperationJson:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = "/Users/mac/PycharmProjects/API_Unittest_Project/dataconfig/user.json"
        else:
            self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        with open(self.file_path) as json_file:
            data = json.load(json_file)
            return data
    def get_json_data(self, id):
        return self.data[id]


    # 写入json
    def write_json(self, data):
        with open("/Users/mac/PycharmProjects/API_Unittest_Project/dataconfig/cookie.json") as fp:
            fp.write(json.dumps(data))

# if __name__ == '__main__':
#     opjson = OperationJson()
#     print(opjson.get_json_data("addcart"))