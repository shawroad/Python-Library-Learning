# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 12:05
# @Author  : xiaolu
# @FileName: 002-公钥加密私钥解密.py
# @Software: PyCharm
import rsa

if __name__ == '__main__':
    with open('pubkey.pem', mode='rb') as f, open('privkey.pem', 'rb') as f1:
        # 从文件读取公私钥
        pub = f.read()
        pri = f1.read()

        # 转为原始的状态
        pubkey = rsa.PublicKey.load_pkcs1(pub)
        privkey = rsa.PrivateKey.load_pkcs1(pri)

    message = '你是个傻逼吧'
    info = rsa.encrypt(message.encode('utf8'), pubkey)
    msg = rsa.decrypt(info, privkey)
    print(msg.decode('utf8'))






