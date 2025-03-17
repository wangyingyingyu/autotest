# 编写一个 Python 程序，接收一个包含学生姓名和成绩的字典，输出成绩最高的学生姓名


def grade(stu_info):
    grade_list=[]
    for stu_grade in stu_info.values():
        grade_list.append(stu_grade)
    max_grade = max(grade_list)
    for i,j in stu_info.items():
        if j == max_grade:
            return f'学生{i}获得了最高成绩{j}'


stu_info = {
    'Tom':87,
    'Eve':98,
    'qiqi':97,
    'xiaoming':88,
    'xiaoxiao':100
}
result = grade(stu_info)
print(result)














