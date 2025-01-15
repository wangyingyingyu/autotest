"""
课堂练习
创建一个 Person 类，定义私有属性 __name 和 __age。
提供封装方法 set_name、set_age 和 get_name、get_age。
添加一个实例方法 introduce，打印出类似 “我叫张三，今年25岁” 的信息。
"""
class Person:

    def __init__(self):
        self.name = ""
        self.age = 0
        self._name = ''
        self._age = 0
        self.__name = ''
        self.__age = 0
    # 修改私有属性
    def set_name(self, name):
        self.__name = name

    def set_age(self,age):
        # 加上年龄判断条件
        if age > 0 :
            self.__age = age
        else:
            return f'年龄必须大于0'
            
    # 获取私有属性
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    # 实例方法 打印信息
    def introduce(self):
        return f'我叫{self.__name}，今年{self.__age}岁'


property_1  =Person()

property_1.set_name('Tom')
property_1.set_age(19)
print(property_1.get_name())
print(property_1.get_age())
print(property_1.introduce())