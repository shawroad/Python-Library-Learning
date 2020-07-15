# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 12:00
# @Author  : xiaolu
# @FileName: 001-rsa生成公私钥并保存.py
# @Software: PyCharm
import rsa

pubkey, privkey = rsa.newkeys(1024)  # 生成公钥和私钥

pub = pubkey.save_pkcs1()   # 将生成的公钥和私钥进行转换, 以便存储
pri = privkey.save_pkcs1()  # save_pkcs1()是内置方法, 其默认参数就是"PEM"

with open('pubkey.pem', mode='wb') as f, open('privkey.pem', mode='wb') as f1:
    f.write(pub)
    f1.write(pri)
