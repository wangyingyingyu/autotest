"""
课后作业
在线课程管理系统
- 增加 Teacher 类，用于管理课程的任课教师，包含姓名和工号属性。
- 修改 Course 类，添加任课教师信息。
- 修改 CourseManager 类，支持分配教师到课程的功能。
- 添加功能：统计每门课程的选课人数排名。
"""
class Teacher:
    def __init__(self, name, id):
        self.name = name
        self.id = id



class Course:
    # 添加课程信息：课程名称、课程指导教师、课程容量、课程已选人数
    def __init__(self,name,teacher,full_num,selected_num):
        self.name = name
        self.teacher = teacher
        self.full_num = full_num
        self.selected = selected_num



class CourseManager:
    # 添加任课教师的信息，创建教师信息字典
    # 以教师id为键key值，以教师信息为value值
    def __init__(self):
        self.teachers = {}
    # 添加教师信息，引入Teacher类的实例对象
    def add_teacher(self,teacher):
        if teacher.id in self.teachers.keys():
            print(f'教师{teacher.name}信息已经存在')
        else:
            self.teachers[teacher.id] = teacher
            print(f'教师{teacher.name}信息添加完成')




























