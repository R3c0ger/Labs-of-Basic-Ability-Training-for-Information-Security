# -*- coding: utf-8 -*-
import binascii

def decode_uuencode(ciphertext):
    plaintext = binascii.a2b_uu(ciphertext)
    print(plaintext.decode())

ciphertext = "89FQA9WMD<V1A<V1S83DY.#<W3$Q,2TM]"
decode_uuencode(ciphertext)