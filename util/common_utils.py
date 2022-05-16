# coding=utf-8
import json
from filecmp import dircmp

class CommonUtil:

    def is_contain(self, str_one, str_two):
        """
        :param str_one:查找的字符串
        :param str_two: 被查找的字符串
        :return:判断两个字符串是否相等
        """
        flag = None
        if isinstance(str_one, str):
            # return str_one.encode("string_escape").decode("unicode-escape")
            return str_one
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, dict_one, dict_two):
        """

        :param dict_one:
        :param dict_two:
        :return: 判断两个字典是否相等
        """
        if isinstance(dict_one,str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        return dircmp(dict_one, dict_two)



