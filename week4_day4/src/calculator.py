"""实战思路
功能描述：
设计一个 Calculator 类，用于进行基本的数学运算，包括加法、减法、乘法和除法。
使用 Pytest 测试框架对 Calculator 类中的每个方法进行单元测试。
测试要求：
使用 pytest 编写测试用例，检查每个运算方法的正确性。
在测试用例中使用断言来验证结果是否符合预期。
配置 PyCharm 来运行 Pytest 测试，并使用界面化操作。"""


class Calculator:
    def add(self,x,y):
        self.x = x
        self.y = y
        return x+y
    def subtract(self,x,y):
        self.x = x
        self.y = y

        return x - y
    def multiply(self,x,y):
        self.x = x
        self.y = y
        return x * y
    def divide_d(self,x,y):
        try:
            return x/y

        except ZeroDivisionError as error:
            return f"除数不能为0{error}"
