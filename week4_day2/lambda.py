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
students.sort(key=lambda stu: stu["name"])
for s in students:
    print(s)

# 以ID降序排序
students.sort(key=lambda stu: stu["id"],reverse=True)
for s in students:
    print(s)


students = [
    {'name': 'Alice', 'id': '1001', 'class': 'Class1'},
    {'name': 'Eve', 'id': '1005', 'class': 'Class2'},
    {'name': 'Charlie', 'id': '1003', 'class': 'Class1'},
    {'name': 'David', 'id': '1004', 'class': 'Class2'},
    {'name': 'Bob', 'id': '1002', 'class': 'Class1'},
    {'name': 'Frank', 'id': '1006', 'class': 'Class2'}
]

def mySorted(obj, key=None, reverse=False):
    newStus = []
    for s in students:
        for n in newStus:
            if key:
                if(key(s) < key(n)):
                    idx = newStus.index(n)
                    newStus.insert(idx, s)
                    break
            else:
                if (s < n):
                    idx = newStus.index(n)
                    newStus.insert(idx, s)
                    break
        else:
            newStus.append(s)

    return newStus if reverse else newStus[::-1]

# students = mySorted(students, key=lambda s: s["name"])
# students.sort(key=lambda s: s["name"])
students = [1,4,2,6,7,8,4,3,3]
students = mySorted(students, reverse=True)
print(students)
for s in students:
    print(s)
