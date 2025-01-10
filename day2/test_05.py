# 编写一个 Python 程序，使用 for 循环，生成并输出斐波那契数列的前 n 项,其中 n 是用户指定的正整数。
# for 循环实现斐波那契  0、1、1、2、3、5、8、13、21、34
"""
def  Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


n = int(input("输入一个正数"))

Fibonacci(n)

def Fibonacci():
    n = int(input("输入一个正整数："))
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    fib  =[1, 1]
    # for i in range(2,n):
    #     num = fib[i-1]+fib[i-2]
    #     fib.append(num)
    # return fib
    for i in range(2,n):
        fib.append(fib[i1]+fib[-2])
    return fib
    for i in range(2,n):# 内存优化，减少对列表的取值
        a, b = b ,a+b

    return fib

Fibonacci()
"""
# 多重赋值tuple unpacking
def Fibonacci(n):
    a =0
    b =1
    for i in range(1,n):
        a, b = b, a+b
        '''
        # b赋值给a，a+b赋值给b，依次循环
        # 左侧两个变量 a,b 右侧b, a+b 生成了一个元组（a, a+b）
        # 第一个元素是当前b的值，第二个元素是当前a 和b之和
        1 a=1 b=1
        2 a=1 b=2
        3 a=2 b=3
        3 a=3 b=5
        4 a=5 b=8
        5 a=8 b=13
        6 a=13 b=21
        7 a=21 b=34 
        '''
        print(a)

n = int(input("输入一个正整数："))
Fibonacci(n)
# 用while 循环逐个打印出序列的值  0、1、1、2、3、5、8、13、21、34
def Fibnacci1():




