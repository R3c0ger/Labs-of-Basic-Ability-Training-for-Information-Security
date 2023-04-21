def caesar_cipher_decrypt(ciphertext):
    for key in range(26):
        plaintext = ""
        for c in ciphertext:
            if c.isalpha():
                plaintext += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
            else:
                plaintext += c
        print(f"Key={key}: {plaintext}")

ciphertext = "FRPHQZSX"
caesar_cipher_decrypt(ciphertext)


def rot13_decrypt(ciphertext):
    key = 13
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            if c.isupper():
                plaintext += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
            else:
                plaintext += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
        else:
            plaintext += c
    print(f"Key={key}: {plaintext}")

ciphertext = "synt{5pq1004q-86n5-46q8-o720-oro5on0417r1}"
rot13_decrypt(ciphertext)
