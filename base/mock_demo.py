# coding=utf-8
from mock import mock

# 模拟mock封装
def mock_test(mock_method, request_data, url, method, response_data):
    # self.run.run_main = mock.Mock(return_value=data)

    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res
