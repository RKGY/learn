animals=['dog','cat','tig','fish','monkey']
animals[-1].title()
print(animals)
#从尾部添加
animals.append('pig')
#插入
animals.insert(1,'elephant')
#删除
del animals[4]#animal.remove('fish')
#删除元素并继续使用它的值
poped=animals.pop(1)
print(poped)
#根据值删除元素
animals.remove('tig')
#排序
animals.sort(reverse=False)
#求长度
print('long='+str(len(animals)))
#list()产生列表,range()函数 产生随机数
numbers=list(range(1,12,2))
print(numbers)
#min() max() sum() 找出最大最小值
min(numbers)
#切片
print(animals[0:3])
#遍历列表
for animal in animals:
    print(animal)

#不可变的列表称为元组
dimensions=(12,54,45,45,3,4,8,25)
#修改元组变量
dimensions=(5,4,3,87,6,4,8,25)
