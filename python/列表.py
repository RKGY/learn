
bicycles=['trek','fsvff','sfsfs','ffds','yyds']
massage="my bicycle was a "+bicycles[-1].title() +"."
print(massage)
bicycles.append('hjhjshj')
bicycles.insert(1,122312)
print(bicycles)
del bicycles[4]#bicycle.remove('ffds')
print(bicycles)
poped=bicycles.pop(1)
print(bicycles)
bicycles.sort(reverse=False)#排序
print(bicycles)
print(len(bicycles))
#遍历列表
for bicycle in bicycles:
    print(bicycle.title())
#range()函数 产生随机数
for value in range(1,5):
    print(value)
#list()产生列表
numbers=list(range(1,12,2))
print(numbers)
#min() max() sum() 找出最大最小值
min(numbers)
#切片
print(bicycles[0:3])
