alien={'color':'green','points':'5'}
#添加键值对
alien['x_position']='0'
alien['y_position']='54'
#遍历字典 item将key与value组成一个元组并返回
for key,value in alien.items():
    print("Key:"+key)
    print("value:"+value+'\n')
#遍历字典中所有键keys().keys()
for name in alien:
    print(name.title())
#set找出列表中独一无二的元素
for name in set(alien):
    print(name.title())