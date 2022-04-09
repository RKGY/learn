#define _CRT_SECURE_NO_WARNINGS
#define _WINSOCK_DEPRECATED_NO_WARNINGS
#pragma warning(disable:6031)

#include<stdio.h>
#include<string.h>
#include<winsock2.h>

#pragma comment(lib,"ws2_32.lib")
#include<windows.h>
#include<iostream>
using namespace std;
//服务器套接字
SOCKET s_socket;
void analysisAdd(char* str);//解析网址
char urlAddr[256];//存放网址
char urlPath[256];//存放网址路径
void snap(char* begAddr);
void connectAddr(char* urlAddr);//连接服务器
void getHtml();//接收源代码并储存
bool download(char* urlAddr);
int web()
{
	char buff[256] = { 0 };
	printf("请输入一个网页链接：");
	scanf("%s", buff);

	snap(buff);

	return 0;
}
void snap(char* begAddr)
{
	analysisAdd(begAddr);
	connectAddr(urlAddr);//连接服务器
	getHtml();

}
void analysisAdd(char* str)
{
	memset(urlAddr, 0, 256);//清空
	memset(urlPath, 0, 256);
	char* p = strstr(str, "http://");//找str中的http:// 找到返回http://的地址
	if (p == NULL)
		return;
	p += 7;
	sscanf(p, "%[^/]%s", urlAddr, urlPath);//格式控制符%[scanfest](^表示匹配到scanfest中的字符结束，-表示从左边到右边之间的所有字符）
	printf("网址：%s\n", urlAddr);
	printf("网址后面的：%s\n", urlPath);
}
void connectAddr(char* urlAddr)//连接服务器
{
	//1.设置网络协议  TCP通讯
	WSADATA wsaDate;
	if (WSAStartup(MAKEWORD(2, 2), &wsaDate) != 0)
	{
		printf("socket 初始化失败！");
	}
	//2.创建socket
	s_socket = socket(AF_INET, SOCK_STREAM, NULL);//socket(协议域，socket类型，指定协议）
	//3.绑定
	SOCKADDR_IN addr = { 0 };
	addr.sin_family = AF_INET;
	int r = bind(s_socket, (sockaddr*)&addr, sizeof(addr));//bind（socket描述字，地址，地址大小）
	if (r == -1)
	{
		printf("绑定失败！\n");
		return;
	}
	printf("绑定成功！\n");
	//4.获取主机ip地址
	struct hostent* p = gethostbyname(urlAddr);
	if (NULL == p)
	{
		printf("获取主机地址失败！\n");
		return;
	}
	printf("获取主机地址成功！\n");
	//5.把服务器的协议地址簇设置好
	memcpy(&addr.sin_addr, p->h_addr, 4);
	addr.sin_port = htons(80);
	//6.连接主机
	r = connect(s_socket, (sockaddr*)&addr, sizeof(addr));
	if (r == -1)
	{
		printf("连接服务器失败！\n");
		return;
	}
	printf("连接服务器成功！\n");
	//7.发请求
	string reqInfo = "GET " + (string)urlPath + " HTTP/1.1\nHost:" +
		(string)urlAddr + "\r\nConnection:Close\r\n\r\n";
	r = send(s_socket, reqInfo.c_str(), reqInfo.size(), NULL);
	if (r <= 0)
	{
		printf("发送失败！\n");
		return;
	}
	printf("发送请求到服务器成功！\n");
}
void getHtml()//接收源代码并储存
{
	string allHtml;//存放网页源代码的字符串
	int r;
	char buff[1024];
	while (1)
	{
		r = recv(s_socket, buff, 1023, NULL);
		if (r > 0)
		{
			buff[r] = 0;//添加结束符号
			allHtml += buff;
		}
		else
		{
			break;
		}
	}
	printf("网页源代码如下:\n");
	cout << allHtml << endl;

}
bool download(char* urlAddr)
{
	CreateDirectory("C:\\Users\\Admin\\Desktop\\生成文件\\resource", NULL);

	return 0;
}

