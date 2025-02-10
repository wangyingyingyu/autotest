# 学生成绩数据
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 55},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 45},
    {"name": "Eve", "score": 72}
]

"""课堂练习：数字列表的处理
从给定的学生成绩数据中，使用列表推导式 筛选出所有及格的学生（成绩大于或等于 60）。
使用字典推导式 构建一个新的字典，字典的键是学生的名字，值是他们的成绩。"""

student1 = [stu for stu in students if stu["score"]>=60]
print(student1)
student2 = {stu["name"]:stu["score"] for stu in students}
print(student2)



