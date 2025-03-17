from week5_day4.src.student_manage_system import Student
import pytest
# def pytest_collection_modifyitems(items) :
#
#
#     for i in items:
#         i.name=i.name.encode("utf-8").decode("unicode_escape")
#         i. nodeid=i.nodeid.encode ("utf-8").decode("unicode_escape")
@pytest.fixture()
def add_stu():
    stu = Student()
    stu.add('01', 'Tom', 18, 'male')
    stu.add('02', 'Eve', 19, 'female')
    stu.add('03', 'David', 20, 'male')
    yield stu