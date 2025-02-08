# 待排序的数据
students = [
    {'name': 'Alice', 'id': '1001', 'class': 'Class1'},
    {'name': 'Eve', 'id': '1005', 'class': 'Class2'},
    {'name': 'Charlie', 'id': '1003', 'class': 'Class1'},
    {'name': 'David', 'id': '1004', 'class': 'Class2'},
    {'name': 'Bob', 'id': '1002', 'class': 'Class1'},
    {'name': 'Frank', 'id': '1006', 'class': 'Class2'}
]
# TypeError: '<' not supported between instances of 'dict' and 'dict'
# students.sort()


# 以名字排序
students.sort(key=lambda stu: stu["name"] + stu['id'])


def sort_by_name_id(stud):
    return stud["name"] + stud['id']


students.sort(key=sort_by_name_id)

# 以ID降序排序
students.sort(key=lambda stu: stu["id"], reverse=True)
for s in students:
    print(s)


def test_fiter():
    a = [1, 2, 3]
    r = filter(lambda x: x > 2, a)
    print(list(r))


def test_fiter2():
    a = [1, 2, 3]

    def greater(x):
        x -= 1
        return x > 2

    r = filter(greater, a)
    print(list(r))
