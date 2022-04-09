import re,requests,time#导入所需要的库

headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
	#"Cookie":"2413a68db7e242364fdb2ff0ecbb5abdea222df93d59499f785d036b5086c289",	
}

detail_urls = []#存储图片地址

for i in range(1,400,20):#20页一张
    url = 'http://www.daimg.com/photo/nature/'.format(i)#请求的地址
    response = requests.get(url,headers,timeout = (3,7))#设置请求超时时间3-7秒
    content = response.content.decode('GB2312')#使用utf-8进行解码
    detail_url = re.findall('"objURL":"(.*?)"',content,re.DOTALL)#re.DOTALL忽略格式#匹配objURL的内容,大部分为objURL或URL
    detail_urls.append(detail_url)#将获取到的图片地址保存在之前定义的列表中
    response = requests.get(url,headers=headers)#请求网站
    content = response.content
b = 0#图片第几张
for page in detail_urls:
    for url in page:
        try:
            print('获取到{}张图片'.format(i))
            response = requests.get(url,headers = headers)
            content = response.content
            if url[-3:] == 'jpg':
                with open('{}.jpg'.format(b),'wb') as f:
                    f.write(content)
            elif url[-4:] == 'jpeg':
                with open('{}.jpeg'.format(b),'wb') as f:
                    f.write(content)
            elif url[-3:] == 'png':
                with open('{}.pon'.format(b),'wb') as f:
                    f.write(content)
            else:
                continue
        except:
            print('超时')
        b +=1