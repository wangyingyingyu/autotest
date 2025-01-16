# for循环实现斐波那契数列
# 实战：for 循环实现斐波那契
# 编写一个 Python 程序，使用 for 循环，生成并输出斐波那契数列的前 n 项,其中 n 是用户指定的正整数。
# 斐波那契数列，又称黄金分割数列，指的是：1、1、2、3、5、8、13、21、34....从第三个数开始，每个数字都是前两个数字之和。
n = int(input('请输入一个数字：'))
fib = [1,1]
for i in range(2,n):
    next_num = fib[i-1] +fib[i-2]
    fib.append(next_num)

print(fib)

