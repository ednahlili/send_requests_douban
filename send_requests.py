# 使用request库调用get请求

import requests
import json


class SendGetRequest:

    def __init__(self, host=None, endpoint=None):
        self.host = "http://127.0.0.1:9999/"
        self.endpoint = "get"

    # 1.不带参数的get请求
    def request_getnoparam(self):
        # str.join(item)
        # 括号里面只能有一个参数
        # 含义是将每一个成员以字符str分隔开再拼接成一个字符串
        # 成员可以是字符串、列表、元组、字典
        url = ''.join([self.host, self.endpoint])
        # 向网页发生请求，并返回状态码
        # get()方法返回一个requests.Response对象。
        response_data = requests.get(url)
        print("不带参数的get请求的返回值如下：\n", response_data)

        # r.text返回HTTP响应内容的字符串形式
        print(type(response_data.text))
        print(response_data.text)
        # eval是内置函数，将字符串当成有效的表达式 来求值并返回计算结果。
        print(eval(response_data.text))

    # 2.带参数的get请求
    def request_getwithparam(self, host=None, endpoint=None):
        url = ''.join([self.host, self.end_point])
        params = {"show_env": "1"}
        r = requests.get(url=url, params=params)
        print(r.text)

    def request_getwithheader(self):
        url = ''.join([self.host, self.endpoint])
        headers = {"User-Agent": "test request headers"}

        r = requests.get(url, headers=headers)
        print(eval(r.text)['headers']['User-Agent'])

    def request_getwithheaderandparam(self):
        url = ''.join([self.host, self.endpoint])
        headers = {"User-Agent": "test request headers"}
        params = {"test_param1": "111", "test_param2": "222"}

        r = requests.get(url, headers=headers, params=params)
        print(r.text)


class SendPostRequest:
    def __init__(self):
        self.host = "http://127.0.0.1:9999/"
        self.end_point = "post"

    def sendpost_with_dataandheader(self):
        url = ''.join([self.host, self.end_point])
        data = {"key1": "value1", "key2": "value2"}
        headers = {"User-Agent": "test post headers"}
        r = requests.post(url, data=data, headers=headers)
        print(r.text)

    def sendpost_uploadfile(self):
        url = ''.join([self.host, self.end_point])
        files = {
            'file': open('testfile.txt', 'rb')
        }
        # 此处不写等号会怎么样？rb是什么模式
        r = requests.post(url, files=files)
        print(r.text)

class Cookie:
    def get_baidu_cookie(self):
        url = "https://baidu.com"
        # get是干什么的
        r = requests.get(url)
        # #将RequestsCookieJar转换成字典
        print(requests.utils.dict_from_cookiejar(r.cookies))

class Session:
    def __init__(self):
        self.host = "http://127.0.0.1:9999/"
        self.end_point = "headers"

    def send_session(self):
        url = ''.join([self.host, self.end_point])
        # url1 = "http://127.0.0.1:9999/cookies/set/sessioncookie/123456789"
        header1 = {"test1":"111"}
        header2 = {"test2":"222"}

        # 初始化一个session对象
        s = requests.session()
        # cookie的信息存在了session中
        s.headers.update(header1)
        r = s.get(url, headers = header2)
        print(r.text, "--------------------")


# send_get_request = SendGetRequest()
# send_get_request.request_getwithheaderandparam()
#
# send_post_request = SendPostRequest()
# send_post_request.sendpost_uploadfile()
#
# cookie=  Cookie()
# baidu_cookie = cookie.get_baidu_cookie()

session_one = Session()
session_one.send_session()