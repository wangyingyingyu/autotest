import pytest
from week6_day5.src.student_system import Student,School


@pytest.fixture()
def add_student_score():
    stu1 = Student("a")
    stu1.add_score("math", 88)
    stu1.add_score("english", 89)
    stu1.add_score("chinese", 90)

    yield stu1

@pytest.fixture()
def school_average():
    stu1 = Student("a")
    stu1.add_score("math", 88)
    stu1.add_score("english", 89)
    stu1.add_score("chinese", 90)
    stu1.cal_average()

    stu2 = Student("b")
    stu2.add_score("math", 97)
    stu2.add_score("english", 91)
    stu2.add_score("chinese", 92)
    stu2.cal_average()
    school = School()
    #school.add_stu(add_student_score())
    school.add_stu(stu1)
    school.add_stu(stu2)
    school.get_grade('a')
    school.get_grade("b")
    school.average()
    yield school
