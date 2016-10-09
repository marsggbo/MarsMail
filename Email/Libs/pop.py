import poplib
from email.parser import Parser

email = "1435679023@qq.com"
password = "19960229hexinABC"
pop3_server = 'pop.qq.com'

server = poplib.POP3_SSL(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))
print("************************************\n\n")
# 身份认证:
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
print("************************************\n\n")
# list()返回所有邮件的编号:
resp, mails, octets = server.list()
# 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
print(mails)
print("************************************\n\n")

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
print(msg_content)
# # 稍后解析出邮件:
msg = Parser().parsestr(msg_content)
data = str(msg)
print("************************************\n\n")

f = open('msg.html','wb')
f.write(data.encode('utf-8'))
f.close()
# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:
server.quit()