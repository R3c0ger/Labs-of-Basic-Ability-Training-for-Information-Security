# -*- coding: utf-8 -*-
def b32de(ciphertext):
    # 去掉数据末尾的等号
    data = ciphertext.rstrip("=")

    # base32编码表
    base32_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"

    # 将base32编码转换为二进制字符串
    bin_data = ''.join([bin(base32_table.index(char))[2:].rjust(5, '0') for char in data])

    # 将二进制字符串按8位分组，超过8位的部分舍去
    bin_strs = [bin_data[byte:byte + 8] for byte in range(0, len(bin_data), 8) if byte + 8 <= len(bin_data)]

    # 将二进制字符串转换为十进制数，再转换为十六进制字节串（bytes类型）
    decoded_data = bytes([int(bin_str, 2) for bin_str in bin_strs])

    # 返回解码后的明文字符串
    return decoded_data.decode()

if __name__ == '__main__':
    ciphertext = "MZWGCZ33MVZGQZLJL5STQOJTGRPWK4SVJ56Q===="
    print(b32de(ciphertext))