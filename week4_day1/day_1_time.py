"""
课堂练习：使用 while 实现倒计时
用户输入一个正整数作为起始值，程序每秒输出一个数字，直到倒计时结束并输出 "倒计时结束！"。
"""
import time
def istime():
    n = int(input('输入一个起始值：'))
    print(n)
    while n > 1:
        time.sleep(1)
        n -= 1
        print(n)
    print('倒计时结束')

istime()