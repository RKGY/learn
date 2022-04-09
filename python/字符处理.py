import re
import socket#正则表达式

#name=input("please enter your name:")
#print("Hello,"+name+"!")
#as取别名
#rstrip()去除末尾空格
string="http://www.cppblog.com/aaxron/archive/2012/04/27/172891.html"
start=re.match("http://",string)
if start:
    url=string[7:]
    end=re.search("/",url).span()
    url=string[7:7+end[0]]
    ip=socket.gethostbyname(url)
    print(ip)

#socket.getaddrinfo(url, None)