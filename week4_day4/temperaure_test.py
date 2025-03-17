"""课堂练习：温度转换器
实现一个简单的温度转换器，可以将摄氏度转换为华氏度，或者将华氏度转换为摄氏度。
摄氏度 (Celsius) 转 华氏度 (Fahrenheit)：通过公式 F = (C * 9/5) + 32，将摄氏度转换为华氏度。
华氏度 (Fahrenheit) 转 摄氏度 (Celsius)：通过公式 C = (F - 32) * 5/9，将华氏度转换为摄氏度。
用 Pytest 测试框架编写单元测试，来验证转换是否正确。"""

def temperature(celsius):

    f = (celsius * 9/5) + 32
    return f


def test_temperature():
    assert temperature(333) == 631.4

def test_temperature2():
    assert temperature(333) == 600