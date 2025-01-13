"""
实战：图书馆借阅管理系统
创建一个类 Library，实现以下功能：
类属性：记录总书籍数量与当前借出的书籍数量。
类方法：
获取当前的书籍状态（总书籍数量、已借出书籍数量、可借书籍数量）。
修改总书籍数量（如新增书籍）。
实现实例方法，用于借书和还书的操作，并同步更新类属性。
模拟图书借阅操作，验证类属性和类方法的正确性
"""
class Library:
    total_num = 10
    lending = 0
    useful_book = total_num-lending

    # 图书馆的名称
    def __init__(self,name):
        self.name = name

    @classmethod
    def book_status(cls):
        print(f'总书记数量：{cls.total_num}')
        print(f'已借出书籍数量{cls.lending}')
        return f'可借书籍数量{cls.useful_book}'
    @classmethod
    def add_book(cls,num):
        cls.total_num += num
        return f'新增了{num}本书籍，总书籍数量为{cls.total_num}'

    def borrow_book(self,borrow_num):
        if borrow_num > Library.useful_book:
            return f'图书馆书籍不足，只能借出{Library.useful_book}本'
        else:
            Library.total_num -= borrow_num
            Library.lending +=borrow_num

            return f'图书馆本次借出{borrow_num}本'

    def return_book(self,num):
        if num > Library.lending:
            return f'还书数量错误'
        else:
            Library.total_num += num
            Library.lending -= num
            return f'还书{num}本'

person1 = Library("京都图书馆")
print(f'图书馆初始状态{Library.book_status()}')
print(person1.borrow_book(4))
print(Library.book_status())
print(person1.return_book(1))
print((Library.book_status()))




















