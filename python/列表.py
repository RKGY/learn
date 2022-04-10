
bicycles=['trek','fsvff','sfsfs','ffds','yyds']
massage="my bicycle was a "+bicycles[-1].title() +"."
print(massage)
#从尾部添加
bicycles.append('hjhjshj')
#插入
bicycles.insert(1,122312)
print(bicycles)
#删除
del bicycles[4]#bicycle.remove('ffds')
print(bicycles)
#删除元素并继续使用它的值
poped=bicycles.pop(1)
print(bicycles)
#根据值删除元素
bicycles.remove('sfsfs')
#排序
bicycles.sort(reverse=False)
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
