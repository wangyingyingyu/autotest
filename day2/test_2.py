"""
a = (1,2,[3])
print(type(a[2]))
print(type(a))

# 可哈希数据
print(hash(123))
print(hash("abc"))
print(hash((1,2,3)))

# 不可哈希数据
print(hash([1,2,3]))
print(hash((1,2,[3])))


# 字典中新增数据 如果key值存在


stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
print(stu)
# 删除元素
del stu['age']
print(stu)
del stu['address']
print(stu)

stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
ks = stu.keys()
print(ks)

stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}

stu.setdefault("hobby1")
print(stu)
stu.setdefault("hobby2", "无")
print(stu)



# 批量生成字典，列表、元组都可以作为keys
# 合并两个字典：dictionary1.update(dictionary2)

# 创建一个员工工资管理系统，使用字典存储每个员工的名字和对应的工资。
# 分别输出所有员工姓名和工资。
# 添加新员工及其工资。
# 更新员工工资。
# 删除员工记录。
# 查找某个员工的工资
# management = {}



management = {
    "Anna": 90,
    "Tom": 78,
    "Jerry": 85,
    "Lucy": 92
}
print(management)
management.setdefault("AAA",99)
print(management)

new = {"Jack":100}
management.update(new)
print(management)
v = management.pop("Anna")
print(v)
print(management)


management.clear()
print(management)



# 创建一个学生成绩管理系统，使用字典存储每个学生的名字和对应的成绩。
# 分别输出所有学生姓名和成绩。
# 添加新学生及其成绩
# 更新学生成绩
# 删除学生记录
# 查找某个学生的成绩
# 初始化学生成绩字典
student_scores = {
    "Anna": 90,
    "Tom": 78,
    "Jerry": 85,
    "Lucy": 92
}

# 1. 获取字典的 key 和 value
all_students = student_scores.keys()
all_scores = student_scores.values()
print("所有学生姓名：", list(all_students))
print("所有学生成绩：", list(all_scores))

# 2. 添加新学生及其成绩
student_scores["Mark"] = 87
student_scores["Eva"] = 80
print("新增学生后字典：", student_scores)

# 3. 更新学生成绩
student_to_update = "Tom"
new_score = 82
if student_to_update in student_scores:
    student_scores[student_to_update] = new_score
    print(f"学生 '{student_to_update}' 的成绩已更新为：{new_score}")
else:
    print(f"学生 '{student_to_update}' 不存在，无法更新成绩。")
print("更新成绩后字典：", student_scores)

# 4. 删除学生记录
student_to_remove = "Jerry"
if student_to_remove in student_scores:
    del student_scores[student_to_remove]
    print(f"学生 '{student_to_remove}' 的记录已删除。")
else:
    print(f"学生 '{student_to_remove}' 不存在，无法删除。")
print("删除记录后字典：", student_scores)

# 5. 查找某个学生的成绩
student_to_find = "Lucy"
if student_to_find in student_scores:
    print(f"学生 '{student_to_find}' 的成绩是：{student_scores[student_to_find]}")
else:
    print(f"学生 '{student_to_find}' 不存在于字典中。")


num = int(input("输入一个整数：\n"))
while num > 0:
    if num % 2 == 0:
        print(0, end="")
    else:
        print(1, end="")
    num = num // 2

print("倒着读为整数的二进制形式")

*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *


*
*  *
*  *  *
*  *  *  *
*  *  *  *  *

*  *  *  *  *
*  *  *  *
*  *  *
*  *
*

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *



for i in range(5):
    for j in range(5):
        print("*",end="  ")
    print()


for i in range(6):
    print("*" * i, end="  ")
    for j in range(5):
        j +=1
    print()

for i in range(6):
    print("*" * (5-i), end="  ")
    for j in range(5):
        j +=1
    print()



for i in range(1, 5):
    kg = 5 -i
    for j in range(kg):
        print(" ", end="  ")

    xh = i*2 -1
    for j in range(xh):
        print("*", end="  ")
    print()

for i in range(5):
    for j in range(5-i-1):
        print(" ", end=" ")
    print("* "*(i*2+1))
print()

"""
text = """
Python is a popular programming language. It is widely used for web development, data science, and more.
Python has a simple and readable syntax, which makes it great for beginners.
"""
words = text.lower().split()
print(words)
word = {}
for i in words:
    if i in word:
        word[i] += 1
    else:
        word = dict.fromkeys(i, 1)

print(word)

for word,count in word.items():
    print(f"单词{word}出现的次数为{count}")
# n = words.count("")
# print(n)


# 定义要统计的文本
text = """
Python is a popular programming language. It is widely used for web development, data science, and more.
Python has a simple and readable syntax, which makes it great for beginners.
"""

# 将文本转换为小写并分割为单词，得到单词列表
words = text.lower().split()
print(f"转换得到的单词列表为：{words}")
# 用于存储单词和出现次数的字典
word_count = {}

# 循环单词列表
for word in words:
    # 去除单词中携带的标点符号
    word = word.strip(".,!?")
    print(f"去除标点之后的单词为 {word}")
    # 如果单词已经在统计字典中，则数量 +1
    if word in word_count:
        word_count[word] += 1
    # 如果单词还没有在统计字典中，则数量设置为 1
    else:
        word_count[word] = 1

# 输出词频统计结果
for word, count in word_count.items():
    print(f"{word}: {count}")



