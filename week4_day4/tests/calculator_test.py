from week4_day4.src.calculator import Calculator
import pytest
"""课堂练习
测试 Calculator 类，该类包含基本的数学运算方法：加法、减法、乘法和除法。
将使用 Pytest 框架来进行单元测试，并展示如何在不同的级别（模块、类、函数）应用 setup 和 teardown。
在模块级别，我们需要打印一些日志，标明模块测试的开始和结束。
每个测试类的开始时，创建一个新的计算器实例，并为类的每个测试方法提供该实例。
为每个测试方法开始和结束打印一些日志。"""
def setup_module():
    print("模块级别的资源开始")
def teardown_module():
    print("模块级别的测试销毁")
class TestCalculator():
    def setup_class(self):
        self.cal = Calculator()
        print("类级别的资源开始")
    def tear_down(self):
        print("类级别的资源销毁")
    def setup_method(self):
        print("方法级别的资源开始")
    def teardown_method(self):
        print("方法级别的资源销毁")
    @pytest.mark.parametrize("x,y,result",[(2,3,5),(-1,1,0)],ids=['2+3=5','-1+1=0'])
    def test_add(self,x,y,result):
        assert self.cal.add(x,y) == result
        # assert self.cal.add(-1, 1) == 0

    @pytest.mark.parametrize("x,y,result", [(5, 3, 2), (0, 1, -1)], ids=['5-3=2', '0-1=-1'])
    def test_subtract(self,x,y,result):
        assert self.cal.subtract(x,y) == result
        # assert self.cal.subtract(0, 1) == -1

    @pytest.mark.parametrize("x,y,result", [(2, 3, 6), (1, 3, 3)], ids=['2*3=6', '1*3=3'])
    def test_multiply(self,x,y,result):
        assert self.cal.multiply(x,y) == result
        # assert self.cal.multiply(0, 100) == 0

    @pytest.mark.parametrize("x,y,result", [(6, 3, 2), (5, 2, 2.5)], ids=['6/3=2', '5/2=2.5'])
    def test_divide_d(self,x,y,result):
        assert self.cal.divide_d(x,y) == result
        # assert self.cal.divide_d(5, 2) == 2.5
"""@pytest.mark.parametrize(
    "变量名", 
    [变量值],
    ids=[用例名]
)
def test_demo(变量名):
    result = 变量名"""


