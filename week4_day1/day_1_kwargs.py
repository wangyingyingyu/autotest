"""
课堂练习：使用可变参数
编写一个函数，接受任意数量的数字参数，返回这些数字的和。
编写一个函数，接受任意数量的关键字参数，返回所有键值对组成的字典。

"""
def func(*args):
    s = sum(args)
    return s

print(func(1,2,3,4))

def func_1(name,age):
    return name,age

result = func_1(name= 'Tom',age=20)
print(result)
# 编写一个函数，能够同时处理位置参数（args）和关键字参数（*kwargs），打印包含位置参数的元组和包含关键字参数的字典。
def func_2(name,**kwargs):
    print(name)
    print(kwargs)
    for i,j in kwargs.items:
        print(i,j)
func_2("tom",age=22,gender="male",address="BeiJing")