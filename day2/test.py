"""
from datetime import datetime

# 定义一个工具类
class Uitls:
    now = datetime.now()

    @classmethod
    def current_datetime(cls):
        return cls.now


    @classmethod
    def current_date(cls):
        '''
        获取当前的年月日
        :return:
        '''
        return cls.now.strftime("%Y-%m-%d")

    @classmethod
    def current_day(cls):
        '''
        获取当前的天
        :return:
        '''
        return cls.now.day

    @classmethod
    def current_time(cls):
        '''
        获取当前的时间
        :return:
        '''
        return cls.now.strftime("%Y-%m-%d")
print(Uitls.current_datetime())
"""
#静态方法
class Calculate:
    @staticmethod
    def sub(num1,num2):
        return num1+num2

print(Calculate.sub(8,9))

class geometry:
    @staticmethod
    def area(lengh,width):
        return lengh*width

    @staticmethod
    def perimeter(length,width):
        return (length+width)*2


print(geometry.area(2,3))
print(geometry.perimeter(2,3))


