"""
课堂练习：图书借阅管理系统
模拟一个图书馆的借阅管理系统。
系统包含以下功能：
使用深拷贝和浅拷贝复制图书信息并演示修改的影响；
检查图书是否在借阅列表中，使用成员运算符 in 和 not in；
使用身份运算符 is 和 is not 比较对象是否为同一本书。
实现以下场景：
借阅列表初始化；
添加图书到借阅列表；
检查某本书是否已被借阅；
复制图书信息并对比深浅拷贝的效果。
"""
# 初始图书列表
library_books = [
    {
        # 书名
        "title": "Python Programming",
        # 作者
        "author": "John Doe",
        # 图书 id
        "id": 101
    },
    {
        "title": "Data Science Basics",
        "author": "Jane Smith",
        "id": 102
    },
    {
        "title": "Machine Learning",
        "author": "Alice Brown",
        "id": 103
    }
]

# 浅拷贝 拷贝内容是原始对象的内层对象的地址引用
import copy
copyLibrary_books = copy.copy(library_books)

print(library_books)
print(copyLibrary_books)

print(id(library_books))
print(id(copyLibrary_books))
print(id(library_books[1]))
print(id(copyLibrary_books[1]))

# 修改浅拷贝过来的数据对原始对象的影响
fix_library_books = copyLibrary_books[1]['author'] = 'Eve'
print(fix_library_books)

print(id(library_books))
print(id(copyLibrary_books))
print(id(library_books[1]))
print(id(copyLibrary_books[1]))
print(id(fix_library_books))

# 深拷贝
import copy
deepCopy = copy.deepcopy(library_books)
print(library_books)
print(deepCopy)

print(id(library_books))
print(id(deepCopy))
print(id(library_books[1]))
print(id(deepCopy[1]))

# 修改深拷贝数据对原始数据的影响
deepCopy[1]['author'] = 'Tom'
print(library_books)
print(deepCopy)

print(id(library_books))
print(id(deepCopy))
print(id(library_books[1]))
print(id(deepCopy[1]))


# 检查图书是否在借阅列表中
def add_book(book):
    books = []
    books.append(library_books[1])
    print(books)

    if lend_book in books:
        print(f'图书{lend_book["title"]}在借阅列表中')
    else:
        print(f'图书{lend_book["title"]}没有在借阅列表中')
    if lend_book['title'] is library_books[1]['title']:
        print(f'为同一本书')
    else:
        print('不为同一本书')
# book_title = []
# for t in books:
#
#     book_title.append(t["title"])
# print(book_title)
lend_book  = {
        "title": "Data Science Basics",
        "author": "Jane Smith",
        "id": 102
        }
add_book(lend_book)