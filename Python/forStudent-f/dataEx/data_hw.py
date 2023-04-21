#!/usr/bin/python
# -*- coding:UTF-8 -*-
import struct


# 题目十七：二进制数据报文构建与解析
def pack_message(data_dict):
    # 判断参数异常或者缺项
    if not isinstance(data_dict, dict): # 判断是否为字典
        return "Parameter Error."
    elif sum(int(i in data_dict) for i in ["type", "csum", "id", "dis1", "dis2", "count"]) != 6: # 判断是否有缺项
        return "Parameter Error."
    elif    not isinstance(data_dict["type"], int) or not isinstance(data_dict["csum"], int) or not isinstance(data_dict["id"], str) \
         or not isinstance(data_dict["dis1"], int) or not isinstance(data_dict["dis2"], int) or not isinstance(data_dict["count"], int):
        return "Parameter Error." # 判断数据类型是否正确
    elif not 0 <= data_dict["type"] <= 100 or not 0 <= data_dict["count"] <= 255: # 判断数据范围是否正确
        return "Parameter Error."
    # try:...except: return "Parameter Error."

    # 按照格式构建报文
    return struct.pack('>BB16sIIB',
                       data_dict['type'],               # 1字节整数
                       data_dict['csum'],               # 1字节校验和
                       bytes(data_dict['id'],'utf-8'),  # 16字节UTF8编码字符串
                       data_dict['dis1'],               # 4字节大端序整数
                       data_dict['dis2'],               # 4字节大端序整数
                       data_dict['count'])              # 1字节整数
    # print(repr(message))

def unpack_message(message):
    try:
        unpacked_message = list(struct.unpack('>BB16sIIB', message))    # 按照格式解包报文
        unpacked_message[2] = unpacked_message[2].decode('utf-8')       # 将16字节UTF8编码字符串转换为字符串
        message_keys = ["type", "csum", "id", "dis1", "dis2", "count"]  # 报文中各个字段的名称，即字典的键
        return dict(zip(message_keys, unpacked_message))                # 使用zip()将键和值组合成字典
    except:
        return "Parameter Error." # 如果解包失败，返回参数异常

if __name__ == "__main__":
    data_dict = {'type': 50, 'csum': 1, 'id': 'abcdefghigklmnop', 'dis1': 300, 'dis2': 100, 'count': 20}
    data = pack_message(data_dict)