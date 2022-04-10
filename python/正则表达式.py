import re#正则表达式

str='Cats45 are smarter than 12dogs'
patterns=[]

#name=input("please enter your name:") #输入

patterns.append(re.match('cats',str,re.I))      #忽略大小写 re.M 多行模式 re.X 为了增加可读性，忽略空格和 # 后面的注释
patterns.append(re.search('[\d]',str))          #匹配数字
patterns.append(re.search('[a-z][\d]*',str))    #*匹配前⼀个字符出现0次或者⽆限次，即可有可⽆
cmp=re.compile('\d')#编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
patterns.append(re.findall('t',str))#在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
patterns.append(re.finditer('\d',str))#在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
patterns.append(re.sub(r"\d+", '998', "python = 997"))#表示替换，将匹配到的数据进⾏替换。
patterns.append(re.subn(cmp, '7', 'fdv45dfv5df'))#返回一个元组 (字符串, 替换次数)
patterns.append(re.split(r":| ","info:xiaoZhang 33 shandong"))#根据匹配进⾏切割字符串，并返回⼀个列表。
#遍历列表
for pattern in patterns:
    if pattern==None:
        print('none')
        continue
    print(pattern)