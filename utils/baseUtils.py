# -*- coding:utf-8 -*-
import requests
import re
import json


class ConfigHttp:
    def __init__(self):
        self.http_name = None
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.module_type = None
        self.secret_key = None
        self.assert_info = None
        self._response = None
        self.re_name = None
        self.re_value = None

    # 接口时用该url
    def set_url(self, api_agreement, object_url, api_url):

        self.url = api_agreement + "://" + object_url + "/" + api_url


    def set_headers(self):
        self.headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        if isinstance(data, str):
            self.data = eval(data)
        elif isinstance(data, dict):
            self.data = data

    def set_files(self, file):
        self.files = file

    def set_re_name(self, re_name):
        self.re_name = re_name

    def set_re_value(self, re_value):
        self.re_value = re_value

    def set_assert_info(self, assert_info):
        self.assert_info = assert_info

    def post(self):
        try:  # json格式时json.dumps(self.data)，form表单的是self.data
            response = requests.post(self.url, data=self.data)
            self._response = response.text
            return response
        except requests.exceptions.ReadTimeout:
            return "发送接口请求超时，请修改timeout时间"

    def get(self):
        try:  # json格式时json.dumps(self.data)，form表单的是self.data
            response = requests.get(self.url, headers=self.headers, params=self.data)
            if response.content:
                self._response = response.text

                return response
            else:
                return None
        except requests.exceptions.ReadTimeout:
            return "发送接口请求超时，请修改timeout时间"

    def assertion(self):
        print(self.assert_info)
        print(type(self._response))
        if self.assert_info in str(self._response):
            return True
        else:
            return False

    def re_func(self):
        print(self.re_value)
        result = re.search(self.re_value, self._response).group(1)
        print(result)
        return result
