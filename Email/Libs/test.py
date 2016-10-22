#!/usr/bin/python
import json
# #Function:Analyze json script
# #Json is a script can descript data structure as xml,
# #for detail, please refer to "http://json.org/json-zh.html".

# #Note:
# #1.Also, if you write json script from python,
# #you should use dump instead of load. pleaser refer to "help(json)".

#json file:
#The file content of temp.json is:
#{
# "name":"00_sample_case1",
# "description":"an example."
#}
def GetLoginInfo():
    f = open("contacts.json",'r',encoding='utf-8')
    s = json.load(f)
    # print(s)
    f.close()
    return s

def SaveLoginInfo(data):
    f = open("contacts.json","w",encoding='utf-8')
    f.write(json.dumps(data))
    f.close()

a = GetLoginInfo()
print(a)
a.pop('test')
SaveLoginInfo(a)



# f = open("../data/241.html",'rb')
# my_email = f.read().decode()
# f.close()

# date = my_email.split("Date: ")[1].split("\n")[0]
# from_addr = my_email.split("From: ")[1].split("\n")[0].split("<")[0].replace(r'"','')
# subject = my_email.split("Subject: ")[1].split("\n")[0]
# emailInfo = date + '\n' + from_addr + '\n' + subject

# print(emailInfo)




# date = my_email.split("Date: ")[1]
# date2 = date.split("\n")[0]
# print(date2)
# print(date)
# print("*****************\n")
# from_addr = my_email.split("From: ")[1].split("To: ")[0]
# # print(from_addr)
# # print("*****************\n")
# subject = my_email.split("Subject: ")[1].split("MIME-Version: ")[0]
# # print(subject)
# # print("*****************\n")
# to_addr = my_email.split("To: ")[1].split("Subject: ")[0]
# # print(to_addr)
# # print("*****************\n")
# # print("Date:%s\nFrom:%s\nSubject:%s\nTo:%s\n"% (date,from_addr,subject,to_addr))


# email = date + '\n' + from_addr + '\n' + subject + '\n' + to_addr
# print(email)






import poplib
from email.parser import Parser

email = "1435679023@qq.com"
password = "19960229hexinABC"
pop3_server = 'pop.qq.com'

class ReceiveMail():
	def __init__(self, parent=None):
		self.emailInfo = {
		"email":"1435679023@qq.com",
		"pwd":"19960229hexinABC",
		"to_addr":"",
		"pop3_server":"pop.qq.com",
		"subject":"",
		"html":"",
		"plain":"",
		}
		self.index = 0

	def Receive(self):
		server = poplib.POP3_SSL(self.emailInfo["pop3_server"])
		server.set_debuglevel(1)
		print(server.getwelcome().decode('utf-8'))
		print("************************************\n\n")
		# 身份认证:
		server.user(self.emailInfo["email"])
		server.pass_(self.emailInfo["pwd"])

		# stat()返回邮件数量和占用空间:
		print('Messages: %s. Size: %s' % server.stat())
		print("1  ************************************\n\n")
		# list()返回所有邮件的编号:
		resp, mails, octets = server.list()
		# resp: 状态码
		# mails：邮件
		# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
		# print("resp:%s\nmails:%s\nocters:%s\n"%(resp, mails, octets))
		# print(mails)
		# print("************************************\n\n")

		# 获取最新一封邮件, 注意索引号从1开始:
		self.index = len(mails)
		for i in range(self.index-9,self.index+1):
			msg_content = ''
			data = ''
			resp, lines, octets = server.retr(i)
			# print("resp:%s\nlines:%s\nocters:%s\n"%(resp, lines, octets))

			# lines存储了邮件的原始文本的每一行,
			# 可以获得整个邮件的原始文本:
			msg_content = b'\r\n'.join(lines).decode('utf-8')
			print(msg_content)
			print("2   ************************************\n\n")
			# # 稍后解析出邮件:
			msg = Parser().parsestr(msg_content)
			data = str(msg)
			print(data)
			print("3   ************************************\n\n")


			f = open('../data/%s.html'%i,'wb')
			f.write(data.encode('utf-8'))
			f.close()
			# 可以根据邮件索引号直接从服务器删除邮件:
			# server.dele(i)
			# 关闭连接:
		server.quit()
		return self.index

# test = ReceiveMail()
# test.Receive()




# for i in range(5,0,-1):
# 	print(i)


# import time, threading

# # 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#     return 123

# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# print(type(t))
# print(t)
# t.join()
# print('thread %s ended.' % threading.current_thread().name)


# f = open('../data/content1.html','rb')
#
# content = f.read()
#
# f.close()

# print(content.decode('utf-8'))



# 处理邮件
 
        # # self.index = ReceiveMail.Receive(self)
        # # print("总邮件数:%d"%self.index)

        # if self.index > 6:
        #     # my_DecodeMail.DecodeMail()
        #     for i in range(self.index,self.index-6,-1):
        #         f = open("../data/%s.html"%str(i),'rb')
        #         my_email = f.read().decode()
        #         f.close()
        #         date = my_email.split("Date: ")[1].split("\n")[0]
        #         from_addr = my_email.split("From: ")[1].split("\n")[0].split("<")[0].replace(r'"','')
        #         subject = my_email.split("Subject: ")[1].split("\n")[0]
        #         emailInfo = date + '\n' + from_addr + '\n' + subject

        #         self.emaillist.addItem(emailInfo)
        # else:
        #     for i in range(self.index+1,0,-1):
        #         f = open("../data/%s.html"%str(i),'rb')
        #         my_email = f.read().decode()
        #         f.close()
        #         date = my_email.split("Date: ")[1].split("\n")[0]
        #         from_addr = my_email.split("From: ")[1].split("\n")[0].split("<")[0].replace(r'"','')
        #         subject = my_email.split("Subject: ")[1].split("\n")[0]
        #         emailInfo = date + '\n' + from_addr + '\n' + subject
        #         self.emaillist.addItem(emailInfo)

a = {}
# a = {
# 	'n1':{
# 		'name':'n1',
# 		'sex':'woman'
# 	},
# 	'marsggbo': {
# 		'name': 'marsggbo',
# 		'sex': 'man'
# 	}
# }
# b = {
# 	'mars':{
# 		'name':'mars',
# 		'sex':'man'
# 	},
# 	'marsggbo':{
# 		'name':'marsggbo',
# 		'sex':'man'
# 	}
# }
# c = {
# 	'mars123':{
# 		'name':'mars123',
# 		'sex':'man'
# 	},
# 	'marsggbo2':{
# 		'name':'marsggbo2',
# 		'sex':'man'
# 	},
# 	'n1':{
# 		'name':'n1',
# 		'sex':'man'
# 	}
# }
# print("更新前")
# print(a)
#
# a.update(b)
# a.update(c)
#
# print("更新后")
# print(a)

#
# a = "你怎么会在这了？这里是华中科技大学啊亲啊！！！(⊙o⊙)哦"
# print(len(a))
# if len(a) > 20:
# 	b = a[:20]
# 	print(len(b))
# 	print(b)
# else:
# 	print(a)
# print(a)