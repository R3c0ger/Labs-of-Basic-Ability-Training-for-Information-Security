# -*- coding: UTF-8 -*-

import base64

#题目十五：Base64编解码
def b64en(path_in, path_out):
    with open(path_in, 'rb') as f:
        data = f.read()
    # encoded_data = base64.b64encode(data).decode() # 使用base64库

    # 将十六进制字符转换为二进制字符串
    bin_data = ''.join([bin(char)[2:].rjust(8, '0') for char in data])
        # print(data) # b'\xff\xd8\xff\xe0\x00\x10......'，十六进制字符形式
        # print(bin_data) # 11111111 11011000 11111111 11100000 00000000 00010000......
    # 如果位数不是6的倍数，则在末尾补0
    if len(bin_data) % 6 != 0:
        bin_data += '0' * (6 - len(bin_data) % 6)
    # 将二进制字符串按6位分组
    bin_strs = [bin_data[byte:byte + 6] for byte in range(0, len(bin_data), 6)]

    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/" # base64编码表
    for i in range(len(bin_strs)):
        # 将每个6字节的二进制字符串转换为十进制数，再转换为base64编码表中对应的字符
        bin_strs[i] = base64_table[int(bin_strs[i], 2)]
    # 合并生成的base64编码字符串
    encoded_data = ''.join(bin_strs)
    # 若base64编码字符串的字节数不是4的倍数，则在末尾补'='
    if len(encoded_data) % 4 != 0:
        encoded_data += '=' * (4 - len(encoded_data) % 4)

    with open(path_out, "w") as f:
        f.write(encoded_data)

def b64de(path_in, path_out):
    with open(path_in, "r") as f:
        data = f.read()

    data = str(data).rstrip("=") # 去掉数据末尾的等号
    base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"  # base64编码表
    # 将base64编码转换为二进制字符串
    bin_data = ''.join([bin(base64_table.index(char))[2:].rjust(6, '0') for char in data])
    # 将二进制字符串按8位分组，超过8位的部分舍去
    bin_strs = [bin_data[byte:byte + 8] for byte in range(0, len(bin_data), 8) if byte + 8 <= len(bin_data)]
    # 将二进制字符串转换为十进制数，再转换为十六进制字节串（bytes类型）
    decoded_data = bytes([int(bin_str, 2) for bin_str in bin_strs])

    with open(path_out, "wb") as f:
        f.write(decoded_data)

if __name__ == '__main__':
    b64en("./pic.jpg", "./pic_en.txt")
    b64de("./pic_en.txt", "./pic_de.jpg")
