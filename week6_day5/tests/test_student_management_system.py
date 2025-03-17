import pytest
from week6_day5.src.student_system import Student,School
class InvalidSubjectError(Exception):
    """自定义异常类，用于处理无效的科目"""
    pass
def setup_module():
    print('学生成绩统计系统打开')
def teardown_module():
    print('学生成绩统计系统关闭')
class TestStudentSystem:
    def setup_class(self):
        self.stu = Student('a')
        print('类测试开始')
    def teardown_class(self):
        print('类测试结束')
    def setup_method(self):
        print('方法测试开始')
    def teardown(self):
        print('方法测试结束')
# 测试要求：使用 pytest 验证成绩的添加、学生平均成绩的计算、班级平均成绩的计算。验证无效成绩的处理。
    @pytest.mark.parametrize("subject,score,result",[('math',90,'添加成绩成功'),
                                                     ("english", 89,'添加成绩成功'),
                                                     ("chinese", 90,'添加成绩成功')],
                             ids=["math","english","chinese"])
    def test_add_score(self,add_student_score,subject,score,result):
        assert add_student_score.add_score(subject,score) == result
    def test_cal_average(self,add_student_score):
        assert add_student_score.cal_average() == '查询成功'
    def test_average_school(self,school_average):
        assert school_average.average() == '查询成功'
    # def test_invalid_score(self):
    #     """测试添加无效科目"""
    #     # example = str(self.stu.add_score('science',100))
    #     # assert example == "捕获到异常: 无效科目science，只能是english,chinese,math"
    #     with pytest.raises(InvalidSubjectError) as excinfo:
    #         self.stu.add_score("physics", 90)
    #     assert "无效科目science，只能是english,chinese,math" in str(excinfo.value)
