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

    def __str__(self):
        return self.name  # 返回教师的名字

class Course:

    # 添加课程信息：课程名称、课程指导教师(引入Teacher类实例对象)、课程容量、课程已选人数
    def __init__(self,course_name,course_teacher,full_num,selected_num):
        self.course_name =course_name
        self.course_teachers = []
        self.course_teachers.append(course_teacher)
        self.full_num = full_num
        self.selected = selected_num

    def __str__(self):
        return str(self.selected)



class CourseManager:
    def __init__(self):
        # 教师信息key值为教师id，value值为教师姓名{id1:name1,id2,name2}
        self.teachers = {}

        # key值为课程名称   value值为课程信息
        self.course = {}

    # 添加教师信息，引入Teacher类的实例对象
    def add_teacher(self, teacher):
        if teacher.id in self.teachers.keys():
            print(f'教师{teacher.name}信息已经存在')
        else:
            self.teachers[teacher.id] = teacher
            print(f'教师 {teacher.name} 信息添加完成')



    # 添加课程信息，调用课程实例化对象
    def add_course(self,add_course):
        if add_course.course_name in self.course.keys():
            print(f'{add_course.course_name} 已经存在课程列表当中')
        else:
            self.course[add_course.course_name] = add_course
            print(f'{add_course.course_name} 课程已经添加到课程列表')

    # 分配教师到课程，引入课程名称字符串，调用Teacher实例化对象
    def delivery_teacher(self,name,teacher):
        if name in self.course.keys():
            if teacher in self.course[name].course_teachers:
                print(f'编号为{teacher.id}的{teacher.name}教师已经在{name}课程的教师名单中')
            else:
                self.course[name].course_teachers.append(teacher)
                print(f'编号为{teacher.id}的{teacher.name}教师添加到了{name}课程中')
        else:
            print(f'课程列表中没有{name}这个课程')




    # 选课 调用课程名字符串
    def selsct_course(self,student_name,name):
        if name in self.course.keys():
            if self.course[name].full_num - self.course[name].selected >= 0:
                print(f'{student_name}选了{name}课程')
                self.course[name].selected -= 1
            else:
                print(f'{name}课程人数已满')
        else:
            print(f'教务系统没有{name}课程')
# 展示课程信息 course_name,course_teacher,full_num,selected_num
    def display_course(self):
        for i in self.course.values():
            teacher_names = ', '.join(str(teacher) for teacher in i.course_teachers) # 获取教师名

            print(f'课程{i.course_name}的指导教师为{teacher_names},'
                  f'课程容量为{i.full_num},已选人数为{i.selected}')

#统计每门课程选课人数排名
    def sort_selected(self):
        selected_arr = {}
        for i in self.course.values():
            selected_arr[i.course_name] = i.selected
        #print(selected_arr)
        # 给选课人数排名
        # 按值排序
        sorted_dict = dict(sorted(selected_arr.items(), key=lambda item: item[1]))
        for name,num in sorted_dict.items():

            print(f'课程{name}已选课人数为：{num}')

# 创建Teacher实例对象
teacher1 = Teacher('Tom','001')
teacher2 = Teacher('Eve','002')
teacher3 = Teacher('qiqi','003')
teacher4 = Teacher('David','004')

# 创建课程类实例对象
course1 = Course('python',teacher1,7,3)
course2 = Course('math',teacher2,8,5)
course3 = Course('English',teacher3,6,2)

# 创建CourseManage类实例对象
manager = CourseManager()
#添加教师信息
manager.add_teacher(teacher1)
manager.add_teacher(teacher2)
manager.add_teacher(teacher3)
#添加课程信息
manager.add_course(course1)
manager.add_course(course2)
manager.add_course(course3)

# 选课
manager.selsct_course('小明','python')
manager.selsct_course('小红','English')

# 分配教师
manager.delivery_teacher('python',teacher4)


# 展示课程信息
manager.display_course()

manager.sort_selected()






