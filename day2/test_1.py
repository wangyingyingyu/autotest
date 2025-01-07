
# 统计查找替换类
length = len("Hello")
print(length)
length = len("Hello World")
print(length)

#
s = "hello world hello Python"
n = s.count("o")
print(n)
n = s.count("O")
print(n)
n = s.count("or")
print(n)
n = s.count("o",10,30)
print(n)

s = "Hello"
print(s.index("l"))
print(s.index("l",0,3)) # 区间使用下标位置，左闭右开区间
print(s.index("k"))

s = "Hello"
print(s.rindex("l"))
print(s.rindex("l",0,3))
print(s.rindex("k"))

s = "Hello"
print(s.find("l"))
print(s.find("l",0,3))
print(s.find("k"))


s = "Hello Hello Hello"
print(s.replace("ll","LL"))
print(s.replace("l","L",4))

url = "https://www.ceshiren.com"
print(url.startswith("https://"))
print(url.startswith("https://", 0, 3))
print(url.startswith("https://", 5, 30))

# 是否包含字母或数字 isalnum() 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True ,否则返回 False
print("abc".isalnum())
print("ABC".isalnum())
print("ABCabc".isalnum())
print("123".isalnum())
print("abc123".isalnum())
print("123abc".isalnum())
print("a b".isalnum())
print("a@".isalnum())
print("".isalnum())

# `\r`是一个转义字符，代表“回车”（Carriage Return）。它的作用是将光标移动到行的开头，而不换行。
print("Hello World Pyth\ron")

# 判断所有单词的首字母是否为大写 不止空格可以为分隔符，_ + 等标点符号或运算符都可为分隔符
print("Username".istitle())
print("User Name".istitle())
print("User_Name".istitle())
print("User.Name".istitle())
print("User+Name".istitle())
print("username".istitle())
print("UserName".istitle())
print("user name".istitle())
print("User name".istitle())

print("this is username".title())
print("THIS IS USERNAME".title())
print("tHIS IS username".title())

print("abc".islower())
print("abc123".islower())
print("ABC".islower())
print("abC".islower())
print("Abc!@#".islower())
print("123".islower())
print("".islower())
print(" ".islower())


# 字符居中和填充
print("|"+"hogworts".center(20) + "|")
print("|"+"hogworts".center(5) + "|")
print("|"+"hogworts".center(20, "-") + "|")

print("a\nb\nc".splitlines())
print("a\nb\nc".splitlines(True))
# 连接可迭代对象(元组、列表、字典中的key)成字符串
l1 = "-".join(("a","b","c"))
print(type(l1))

print("".join(["a","b","c"]))

print("-".join(("a","b",1)))  # 报错

print("->".join(("a","b","c")))
print("->".join(["a","b","c"]))
print("->".join({"a","b","c"}))
print("->".join({"a":"A","b":"B","c":"C"}))


s = "abcdefg"

# 普通切片
print(s[0: 2])
# 省略范围
print(s[0:])
print(s[: 2])
print(s[:])

# 指定步长
print(s[::1])
print(s[::2])

# 负下标
s = "abcdefg"
print(s[-3: -1])
# 负步长
print(s[-1: -3: -1])
# 逆序
print(s[::-1])


l = [1,2,3,4,5]
length = len(l)

l = [1,2,3,4,5,1,2,3,3]
print(l.count(3))

l = [1,2,3,4,5,1,2,3,3]
print(l.index(3))
print(l.index(3,5,10))

l = []
l.append(1)
print(l)
l.append(1)
print(l)
l.append(2)
print(l)

l1 = [1,2,3]
l2 = ["a","b","c"]

l1.append(l2)
print(l1)
l1.extend(l2)
print(l1)
l1.extend("456")
print(l1)
l1.extend(("A","B","C"))
print(l1)

l = [1,2,3,4,5]

l.insert(0, "A")
print(l)
l.insert(3, "B")
print(l)
l.insert(10, "C")
print(l)
l.insert(9, "D")
print(l)
l = [1,2,3,4,5,1,2,3]
del l[0]
print(l)
del l[10]

l = [1,2,3,4,5,1,2,3]
l.remove(3)
print(l)
l.remove(33)

l = [1,2,3,4,5,1,2,3]
print(l.pop())
print(l)
print(l.pop(3))
print(l)
print(l.pop(10))

l = [1,2,3,4,5,1,2,3]
l.clear()
print(l)


l = ["a","abc","ab","A"]
l.sort()
print(l)
l = ["a","abc","ab","A"]
l.sort(reverse=True)
print(l)


# 编写一个Python程序，输入一个5位数，判断输入的这个数字是否为回文数。
# 回文数是指从左到右和从右到左读都一样的数。例如12321。如果输入的是回文数，输出是回文数，否则输出不是回文数。
num = input("请输入一个五位数：")
num_1 = int(num[::-1])
print(num_1)
# 检查回文
if int(num) == num_1:
    print(f"输出回文数为 {num}")
else:
    print("你输入的不是回文数")

# 编写一个Python程序，对一个简单的故事进行如下操作：
#
# 统计故事中的单词数量。
# 查找主人公的名字在故事中的位置。
# 将主人公的名字替换为你的名字。
# 将故事改写为大写和小写形式。
story = "Once upon a time, in a land far away, lived a brave knight named Arthur."
a = story.split()
print(a[0])
b = ("".join((a[0],a[1],a[2])))
print(b)
print(f"统计故事中的单词数量:{len(b)}")
print(f"查找主人公的名字在故事中的位置:{story.find('Arthur')}")
new = story.replace("Arthur","Brave")
print(f'将主人公的名字替换为你的名字{new}')

story = "Once upon a time, in a land far away, lived a brave knight named Arthur."
list =story.split()
print(type(list))
print(len(list))

l1 = list("abc")
l2 = list((1,2,3))
l3 = list([1,2,3])
print(l1)
print(l2)
print(l3)

#在给定的学生列表 students 中完成以下操作：
# - 统计当前学生总人数。 - 添加两名新学生："Mark"（87分）和 "Eva"（80分）。 - 删除第 2 位学生的记录
students = [["Anna", 90], ["Tom", 78], ["Jerry", 85], ["Lucy", 92]]
num = len(students)
print(f'统计当前学生总人数为:{num}')
students.append(["Mark", 87])
students.append(["Eva", 80])
print(f'添加两名新学生{students}')

del students[1]
print(students)

# 管理一个书籍列表，可以实现以下功能： - 统计当前书籍总数。 - 增加新书籍到列表。 - 删除已存在的书籍。 - 对书籍列表按字母顺序排序。
# 输出每次操作后的书籍列表和对应的提示信息

books = ["Python Programming", "Data Structures", "Artificial Intelligence", "Web Development"]
print(f'统计当前书籍总数为:\n {len(books)}')
books.append("Machine Learning")
print(f'增加"Machine Learning"书籍到列表:\n {books}')
books.remove("Python Programming")
print(f'删除"Python Programming"书籍:\n {books}')
books.sort()
print(f'对书籍列表按字母顺序排序\n {books}')










