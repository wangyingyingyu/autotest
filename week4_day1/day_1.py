"""
课堂练习：简单的成绩判断
用户输入 3 门课程的成绩，存储到一个列表中。
计算总分和平均分。
如果平均分大于等于 60，则输出“及格”，否则输出“不及格”。
"""
def grade():
    grade = []
    grade.extend(input('输入你的三门成绩：'))
    grade_num = []
    for i in grade:
        grade_num.append(int(i))
    print(grade_num)
    sum_num = sum(grade_num)
    average = sum_num / len(grade_num)

    if average >= 60:
        print(' 及格')
    else:
        print('不及格')

grade()
l1 = [1,2,3]
l2 = ["a","b","c"]

l1.append(l2)
print(l1)
l1.extend(l2)
print(l1)
l1.extend('456')
print(l1)
l1.extend(("A","B","C"))
print(l1)



