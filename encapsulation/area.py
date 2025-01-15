"""
课堂练习
创建一个基础类 Shape，包含一个方法 area()。
创建派生类 Circle 和 Rectangle，继承 Shape 并实现自己的 area() 方法。
使用多态调用 area() 方法来计算不同形状的面积。
"""
import math
class Shape:
    def area(self):
        return f'计算面积'


class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):

        return f'圆的面积为{math.pi*(self.r**2)}'


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):

        return f'矩形面积为{self.w*self.h}'

class result:
    def area(self,shape):
        shape.area()

shapes = [
    Circle(5),      # 半径为 5 的圆
    Rectangle(4, 6) # 宽为 4 高为 6 的矩形
]

for shape in shapes:
    print(f'Shape area: {shape.area()}')













