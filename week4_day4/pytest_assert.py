import pytest


def func(x):
    return x+1
def test_assert():
    assert func(2) == 5

#`pytest.mark.parametrize` 是 Pytest 中用于参数化测试的一个装饰器。
# 它允许你定义多个输入参数和期望结果，从而自动生成多个测试用例。
def add(a,b):
    return a+b
# 定义参数 参数名 参数值         第一个参数是由逗号分隔的字符串表示参数名 第二个参数是包含参数元组的列表，每个元组表示一组参数及其期望输出
@pytest.mark.parametrize("a,b,expected",[(1,2,3),(2,2,5),(1,3,6)])
#测试函数 `test_add` 接收 `a`、`b` 和 `expected` 作为参数。Pytest 会为列表中的每个元组生成一个独立的测试用例。
def test_add(a,b,expected):
    assert a+b == expected
