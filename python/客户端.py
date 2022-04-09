import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
filename="C:\\Users\\Admin\\Desktop\\生成文件\\接收数据.jpg"
l = s.recv(1024)

leng=eval(l)
recver=0
with open(filename,"wb") as file:
    while leng-recver>1024:
        msg=s.recv(1024)
        recver+=len(msg)
        file.write(msg)
    msg+=s.recv(leng-recver)
    file.write(msg)
print(int(l))



s.close()

#print (msg.decode('utf-8'))