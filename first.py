# 课后作业  #编写一个 Python 程序
# 用户输入一个分数，程序将根据分数判断并输出相应的等级。
# 分数在 90 分及以上为 A 等级，60 -89 分为 B 等级，否则为 C 等级
grade = float(input("请输入你的分数：\n"))
if grade < 90:
    if grade >= 60:
        print("你的成绩为B等级")
    else:
        print("你的成绩为C等级")
else:
    print("你的成绩为A等级")


"""
a = 5
b = 10

a = a + b
b = a - b
a = a - b
print(a)
print(b)

a = 5
b = 10

a, b = b, a
print(a, b)

# 需求：编写一个简单的 Python 程序，支持加减乘除四种运算。
# 需求分析：用户输入两个数字和一个运算符，程序计算并输出结果。
num_1  =  int(input("请输入第一个数字：\n"))
num_2 = int(input("请输入第二个数字：\n"))
operator  =  input("请输入运算符：\n")
if operator == "+":
    print(num_1 + num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    if num_1 != 0:
        print(num_1 / num_2)
    else:
        print("除数不能等于0！")
elif operator == "-":
    print(num_1 - num_2)
else:
    print("无效运算符！")

balance = float(input("请输入公交卡当前余额：\n"))
if balance >= 2:
    seat = int(input("车上有空位选 1 ，车上没空位选 0 :\n"))
    if seat == 1:
        print("请上车")
    else:
        print("抱歉，车上没有空位，请下车")
else:
    print("余额不足，请下车")


name = input("请输入你的名字：\n")
hobby = int(input("请选择你擅长/喜欢的科目，文科选1，理科选2：\n"))
if hobby == 1:
    orientation_choose = int(input("请选择你想要的职业，历史选1，地理选2：\n"))
    if orientation_choose == 1:
        orientation = "历史"
    else:
        orientation = "地理"
else:
    orientation_choose = int(input("请选择你想从业的方向：数学选1，生物选2，编程选3\n"))
    if orientation_choose == 1:
        orientation = "数学"
    elif orientation_choose == 2:
        orientation = "生物"
    else:
        coder_choose = int(input("请选择你想从事的软件职业方向：测试选1，开发选2，产品选3，项目经理选4\n"))
        if coder_choose == 1:
            orientation = "测试"
        elif coder_choose == 2:
            orientation = "开发"
        elif coder_choose == 3:
            orientation = "产品"
        else:
            orientation = "项目经理"
print(f"{name} 同学，你意向的职业为: {orientation}")


霍格沃兹测试开发学社

# print("测试开发进阶，首选霍格沃兹！")
#
# # 输入函数
# username  = input("请输入用户名：")
# print( username, "欢迎您~")
# 数据类型 字符型str 整数型 int 浮点数型 float 布尔型 bool
num = "20"
print(type(num))
print(int(num))
print(type(int(num)))

# 运算符
a = 10
b = 20
result = a + b
print("加法运算：", result)
result_1 = b-a
print("减法运算：", result_1)
result_3 = a * b
print("乘法运算：", result_3)
c = 66
d = 30
print("整除：", c // d)
print("取余：", c % d)

# 赋值运算符 = - * / += -= *= /=
e  = 3
e += 10
print(e)

e -= 10
print(e)
e *= 10
print(e)
e /= 10
print(e)

e %= 10
print(e)
e **= 10
print(e)
e = 2
e *= 3+4
print(e)


print( 1 == 2)
print( 1 == 1)
print( 1 == "2")
print( 2 == "2")
print( "abc" == "abc")
print( "abc" == "ABC")

print( 1 != 2)
print( 1 != 1)
print( 1 != "2")
print( 2 != "2")
print( "abc" != "abc")
print( "abc" != "ABC")

print( 1 > 2)
print( 1 > 1)
print( 1 > "2")
print( 2 > "2")
print( "abc" > "abc")
print( "abc" > "ABC")

print( 1 < 2)
print( 1 < 1)
print( 1 < "2")
print( 2 < "2")
print( "abc" < "abc")
print( "abc" < "ABC")
# 大于等于
print( 1 >= 2)
print( 1 >= 1)
print( 1 >= "2")
print( 2 >= "2")
print( "abc" >= "abc")
print( "abc" >= "ABC")
# 小于等于
print( 1 <= 2)
print( 1 <= 1)
print( 1 <= "2")
print( 2 <= "2")
print( "abc" <= "abc")
print( "abc" <= "ABC")

a = input("请输入三位数字：")
b = int(a)
e = b // 100
c = (b % 100 ) // 10
d  = (b % 100 ) % 10
print("输出的数字为:", e + c * 10 + d * 100)

# print(d, c, e, sep="")


"""




