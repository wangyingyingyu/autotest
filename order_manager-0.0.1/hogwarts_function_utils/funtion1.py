import inspect

a = 1
b = 2

print(a + b)

c = 0


def divide(x, y):
    """
    除法
    :param x:
    :param y:
    :return:
    """
    a = 1
    b = 2


    def fun1():
        m = 1
        return m

    return x / y


def run():
    for i in range(-10, 10):
        print(i)
        result = divide(x=a, y=i)
        print(result)


run()
