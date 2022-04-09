import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(1)
filename="C:\\Users\\Admin\\Desktop\\source\\晚萤.jpg"
with open(filename,'rb')as file:
        re=file.read()
print(len(re))
while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()

    print("连接地址: %s" % str(addr))
   
   
    clientsocket.send(str(len(re)).encode("utf-8"))
    clientsocket.send(re)

    clientsocket.close()