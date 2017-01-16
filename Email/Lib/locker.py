#coding=utf-8
import base64

# 加密
def encrypt(code):
	return base64.encodebytes(code.encode('utf-8')).decode('utf-8')

# 解密
def decrypt(code):
	return base64.decodebytes(code.encode('utf-8')).decode('utf-8')

