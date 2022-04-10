import re#正则表达式

str='Cats45 are smarter than 12dogs'
patterns=[]

#name=input("please enter your name:") #输入

patterns.append(re.match('cats',str,re.I))      #忽略大小写 re.M 多行模式 re.X 为了增加可读性，忽略空格和 # 后面的注释
patterns.append(re.search('[\d]',str))          #匹配数字
patterns.append(re.search('[a-z][\d]*',str))    #*匹配前⼀个字符出现0次或者⽆限次，即可有可⽆
#遍历列表
for pattern in patterns:
    if pattern==None:
        print('none')
        continue
    print(pattern)