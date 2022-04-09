alien={'color':'green','points':'5'}
#访问字典中的值
print(alien['color'])
#添加键值对
alien['x_position']='0'
alien['y_position']='54'
#遍历字典
for key,value in alien.items():
    print("\nKey:"+key)
    print("\nvalue:"+value)
#遍历字典中所有键keys()
for name in alien.keys():
    print(name.title())