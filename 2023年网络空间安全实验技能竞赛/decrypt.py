# 未完成
import base64

# 定义加密函数 _cipher 的逆函数，即解密函数 _decipher
def _decipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65   # 根据字母大小写确定 ASCII 码偏移量
            ascii_code = ord(char)                        # 获取字符的 ASCII 码值
            shifted_code = ((ascii_code - ascii_offset + shift) % 26 + ascii_offset)  # 计算移位后的 ASCII 码值
            shifted_char = chr(shifted_code)              # 将 ASCII 码值转换为字符
            result += shifted_char                        # 拼接解密后的字符
        else:
            result += char                                # 直接拼接非字母字符
    return result

# 定义解密函数 decrypt_ciphertext，对密文进行解密
def decrypt_ciphertext(ciphertext):
    decoded_text = _decipher(ciphertext, 15)             # 先进行逆循环移位操作，偏移量为 15
    encoded_text = base64.b64decode(decoded_text)        # 使用 base64 进行解码
    # 将编码后的字符串转换回十六进制编码，再解码为原始明文
    plaintext = encoded_text.hex()
    return plaintext

# 测试代码
ciphertext = "TpE2EfEdTpi3EpXrTZi1SJA1TCE0SfAfSfOfSJSeSfS3FJOcTfq2Fpi1TfO0UZW0S2KfSpScSfOfSZSfSfGfSfScSfqfSW=="
plaintext = decrypt_ciphertext(ciphertext)
print(plaintext)