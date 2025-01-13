"""
课后作业
- 创建一个学生成绩管理系统，学生的信息包括 姓名（字符串）、课程名称和成绩。
- 使用函数封装每个功能。
- 主菜单展示系统功能。
- 添加学生成绩（学生姓名、课程名称、成绩）。
- 查询某个学生的成绩。
- 更新学生的成绩。
- 删除学生的成绩记录。
- 显示所有学生的成绩。

# 主菜单展示信息

学生成绩管理系统






6. 退出系统
"""

stu_management = {
    'aa': {'name':'aa','subject':'math','grade':90},
    'bb':{'name':'bb', 'subject':'English','grade':91},
    'cc':{'name':'cc','subject': 'Chinese','grade':98}
}
#1. 添加学生成绩
def add_grade(name,subject,grade):

    stu_management[name] = {'name':name,'subject': subject, 'math':grade}
    print(f'添加学生{name}的{subject}成绩为{grade}\n 修改后的学生信息为：')
    return stu_management
# 2. 查询学生成绩

def query (name):
    # print(stu_management.get(name,"该学生不存在"))
    return stu_management.get(name,"该学生不存在")

# 3. 更新学生成绩
def update_grade(name,subject,grade):
    if name in stu_management.keys():
        stu_management[name]['grade'] = grade
        km = stu_management[name]['subject']
        print(f'更新学生{name}的{km}成绩为{grade}\n 修改后的学生信息为：')

    else:
        print(f'学生{name}不存在')
    return stu_management

# 4. 删除学生成绩记录

def remove_student(name):
    if name in stu_management.keys():
        del stu_management[name]
        print(f"学生 '{name}' 的记录已删除。")
    else:
        print(f"学生 '{name}' 不存在，无法删除。")
    return stu_management

# 5. 显示所有学生成绩
def show_all():
    return stu_management.values()

add_stu = add_grade("ee", "science",98)
print(add_stu)
search = query("aa")
print(search)
update = update_grade("bb","English",97)
print(update)
remove = remove_student("bb")
print(remove)
all_grade = show_all()
print(all_grade)