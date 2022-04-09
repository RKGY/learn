
from multiprocessing import connection
import re
import time
from bs4 import BeautifulSoup
import requests

#url=input("请输入一个网址：")
url="http://10.254.8.1:8089/?s=c7d825ea2b405ffdbafc489278b07485&mac=45080e24e39e7a2f28d9a1c2dea9bbed&vid=0706cc51d695d9d3&port=3120cd184ac99a20&url=709db9dc9ce334aa02a9e1ee58ba6fcf3bc3349e947ead368bdd021b808fdbac30c65edaa96b0727&userip=6e2be4ecc37f2255c1fede211d6de8c3&ssid=bb0bd32f8b8fd874"
if re.match('http://',url):
    ip=url[7:]
    addr=url[:re.search('/',ip).span()[0]+7]
elif re.match('https://',url):
    ip=url[8:]
    addr=url[:re.search('/',ip).span()[0]+8]
else:
    addr='http:/'
#发请求
proxies={'http':'101.95.60.32:80',
'https':'118.31.1.154:80'
}
try:
    
    if requests.get(url).status_code==200:#,proxies=proxies
        print('ip可用')
except:
    print('ip不可用')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46",
'connection':'close'
}
params = {"wd":"校园",
"pn":0
}
filename="C:\\Users\\Admin\\Desktop\\生成文件\\图片\\"
detail_urls=[]#储存列表

responses=requests.get(url,headers=headers)#,proxies=proxies
responses.encoding=responses.apparent_encoding
html_text=responses.text
soup=BeautifulSoup(html_text,'html.parser')
urls=soup.find_all('a',target="_blank")#,class_="pic"
print(responses.status_code)
#首个数据url	
for URL in urls:
    requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
    get_url = requests.session()
    get_url.keep_alive = False
    time.sleep(1)
    if re.findall('http',URL.get('href'))==[]:
        responses=get_url.get(addr+URL.get('href'),headers=headers)
    else:
        responses=get_url.get(URL.get('href'),headers=headers)
   
    
    responses.encoding=responses.apparent_encoding#设置编码
    html_text=responses.text
    soup=BeautifulSoup(html_text,'html.parser')
    try:
        
        detail_urls=soup.find_all('img')
        if detail_urls==[]:
            continue
        #遍历标签
        for i in detail_urls:
            name=i.get('alt')
            if i.get('src')==None:
                    href=i.get('lazysrc')
            else:
                href=i.get('src')
            print(href)
            if re.findall('http',href)==[]:
                href=addr+i.get('src')
            requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
            s = requests.session()
            s.keep_alive = False # 关闭多余连接
            
            img_resp=s.get(href,timeout=1)
            if img_resp.status_code!=200:#访问失败跳过
                continue
            #下载文件
                

            tupian=img_resp.content
            #tupian_name=href.split('/')[-1]

            with open(filename+name+'.jpg',"wb") as file:
                file.write(tupian)
        

        # 查看响应码
        

        # 接收的数据

        
    except:
        print('没有找到图片！')