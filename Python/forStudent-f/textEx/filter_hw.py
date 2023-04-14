# -*- coding: UTF-8 -*-

import os
import re

# 题目十三：C程序文件处理
def filter_c_file(dir_path):
    # 创建该目录下所有C程序的路径的列表。
    cfile_list = []
    for root, dirs, files in os.walk(dir_path):  # os.listdir()方法不包括 . 和 .. ，即使它在文件夹中。
        for file in files:
            # 判断文件后缀名是否为.c或.cpp。
            if os.path.splitext(file)[-1] == '.c' or os.path.splitext(file)[-1] == '.cpp':  # os.path.splitext 比 .split() 效率更高。
                cfile_list.append(root + "/" + file)  # os.path.join(root, file)也行，但是路径分隔符不统一。

    # 对每个C程序的内容进行处理。
    for file in cfile_list:
        with open(file, 'r', encoding='utf-8') as f:  # 考虑到中文注释，设定打开文件时所使用的编码格式为utf-8。
            f = f.read()
            f = re.sub(r'#include\s*<.*?>', '', f)  # 使用正则表达式去除include语句
            f = re.sub(r'/\*[\s\S]*?\*/', '', f)    # 去除块注释
            f = re.sub(r'//.*', '', f)              # 去除行注释
            f = re.sub(r'\s+', '', f)               # 去除代码中的空格、空行、回车换行符号
            # 将处理后的C程序字符串写入新文件中。
            new_file_name = os.path.splitext(file)[0] + '.txt'
            with open(new_file_name, 'w', encoding='utf-8') as new_file:
                new_file.write(f)

if __name__ == '__main__':
    dir_path = "./testData"
    filter_c_file(dir_path)
