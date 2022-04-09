class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        #初始化属性
        self.name=name
        self.age=age
    def sit(self):
        #模拟小狗蹲下
        print(self.name.title()+"is now sitting")
    def roll_over(self):
        #模拟小狗打滚
        print(self.name.title()+"rolled over!")
d=Dog('lids',12)
print(d.name)