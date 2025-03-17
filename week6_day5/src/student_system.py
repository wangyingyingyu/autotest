import math
# """实战：学生成绩统计系统
# 设计一个学生成绩管理系统，支持添加成绩、计算平均分和学校级别的平均分。

# 表示一个学生的属性和方法
class InvalidSubjectError(Exception):
    """自定义异常类，用于处理无效的科目"""
    pass
# 学生类 (Student)：表示学生，包含学生姓名和各科成绩。方法包括添加单个科目的成绩和计算学生的平均成绩。
class Student:
    def __init__(self,name):
        self.name=name
        # {"subject":score,"subject":score}
        self.grade = {}
        # 输入要添加的学生对应科目的成绩
    def add_score(self,subject,score):
        try:
            if subject not in ["english","chinese","math"]:
                #raise InvalidSubjectError(f'无效科目{subject}，只能是english,chinese,math')
                raise f'无效科目{subject}，只能是english,chinese,math'

            if  not isinstance(score, (int, float)):
                raise ValueError(f"成绩{score}必须是数字")
            if score<0 or score>100:
                raise ValueError(f"成绩{score}超出正常分数范围")
            self.grade[subject]=score
            print('添加成功')
            return '添加成绩成功'
        except Exception as e:
            print(e)

        # 添加成绩的方法
    def add_score1(self, subject, score):
        if subject not in ["english", "chinese", "math"]:
            raise InvalidSubjectError(f'无效科目{subject}，只能是english,chinese,math')

        if not isinstance(score, (int, float)):
            raise ValueError(f"成绩{score}必须是数字")
        if score < 0 or score > 100:
            raise ValueError(f"成绩{score}超出正常分数范围")

        self.grade[subject] = score
        print('添加成功')
        return '添加成绩成功'

    def cal_average(self):
        grades = []
        for i in self.grade.values():
            grades.append(i)
        average_score = sum(grades)/len(grades)
        # self.grade["平均成绩"]=average_score
        print(f'学生{self.name}的平均成绩为{average_score}')
        return '查询成功'
# 学校类 (School)：管理学生信息，支持添加学生、获取特定学生的成绩，并计算全校的平均成绩。
class School:
    def __init__(self):
        self.all_student = {}
       # {name:{},
    #     name:{}
    #     }
    def add_stu(self,stu):
        if stu.name not in self.all_student:
            self.all_student[stu.name]=stu.grade
            print(self.all_student)
            return '添加成功'
        print(f'学生{stu.name}已经存在')
        return '添加不成功'
    def get_grade(self,name):
        if name in self.all_student:
            print(f'学生{name}的成绩表为{self.all_student[name]}')
            return '查询成功'
        else:
            print(f'学生{name}不存在')
            return '查询不成功'

    def average(self):
        try:
            all_grade=[]
            for i in self.all_student.values():
                j=sum(i.values())
                all_grade.append(j)
            average_all_stu = sum(all_grade)/len(all_grade)
            print(f'学校学生平均成绩为{average_all_stu}')
            return '查询成功'
        except Exception as e:
            print(e)
            return '查询失败'
if __name__ == "__main__":
    stu1=Student("a")
    stu1.add_score("math",88)
    stu1.add_score("english",89)
    stu1.add_score("chinese", 90)
    try:
        s = stu1.add_score1("mat", 99)  # 使用无效科目"mat"
        print(str(s))
    except InvalidSubjectError as e:
        print(f"捕获到异常: {e}")
    except ValueError as ve:
        print(f"捕获到异常: {ve}")

    stu1.cal_average()
    stu2=Student("b")
    stu2.add_score("math", 97)
    stu2.add_score("english", 91)
    stu2.add_score("chinese", 92)
    stu2.cal_average()
    school=School()
    school.add_stu(stu1)
    school.add_stu(stu2)
    school.get_grade('a')
    school.get_grade("b")
    school.average()





















