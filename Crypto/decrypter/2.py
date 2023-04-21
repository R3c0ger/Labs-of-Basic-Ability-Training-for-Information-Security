def fence_decrypt(ciphertext):
    # 获取密文长度
    n = len(ciphertext)

    # 遍历栏数，尝试解密
    for num_rails in range(2, n):
        fence = [[None] * n for i in range(num_rails)] # 生成栏数×密文长度的二维数组
        rails = list(range(num_rails - 1)) + list(range(num_rails - 1, 0, -1))
        for i, c in enumerate(ciphertext):
            fence[rails[i % num_rails]][i] = c
        plaintext = ''.join([c for rail in fence for c in rail if c is not None])
        print(f"Key={num_rails}: {plaintext}") # f表示格式化字符串，{}中的变量会被替换为变量值

ciphertext = "fsf5lrdwacloggwqi11l"
fence_decrypt(ciphertext)