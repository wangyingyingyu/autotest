"""
实战：图书管理系统
创建一个图书管理系统，实现以下功能
1. 图书类 Book：属性包括书名（title）、作者（author）和出版日期（publish_date），方法包括获取书名、获取作者和获取出版日期的方法。
2. 图书馆类 Library：属性包括图书列表（books），方法包括添加图书、借出图书、归还图书和显示所有图书的方法。
3. add_book 方法：接受一个 Book 类型的参数，将其添加到图书列表中。
4. borrow_book 方法：接受一个字符串类型的参数（书名），找到对应书名的图书，并将其从图书列表中移除。
5. return_book 方法：接受一个 Book 类型的参数，将其添加到图书列表中。
6. show_books 方法：输出当前图书馆中所有图书的书名、作者和出版日期。
"""

class Book:
    def __init__(self,title,author,publish_date):
        self.title  = title
        self.author = author
        self.publish_date = publish_date
    def title(self):
        return f'这本书的书名为{self.title}'
    def author(self):
        return f'这本书的作者为{self.author}'
    def publish_date(self):
        return f'这本书的出版日期为{self.publish_date}'



class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):

        self.books.append(book)

        return f'已将{book.title}添加到图书馆'

    def borrow_book(self,book2):
        for book in self.books:
            if book2 == book:
                self.books.remove(book)
            else:
                return f'图书馆不存在{book2}'


    def return_book(self,book3):
        for book in self.books:
            if book == book3:
                return f'{book3}已存在图书馆'
            else:
                self.books.append(book3)
                return f'已将{book3.title}归还到图书馆'



    def show_books(self):
        for book in self.books:
            return f'这本书的书名为{book.title},这本书的作者为{book.author},这本书的出版日期为{book.publish_date}'



# 实例化Book对象
book_1 = Book('西游记','吴承恩','2000-1-1')
book_2 = Book('红楼梦','曹雪芹','2000-1-2')

# 实例化图书馆对象
library = Library()

#library.add_book(book_1)
print(library.add_book(book_2))

print(library.show_books())

print(library.borrow_book('红楼梦'))
print(library.return_book(book_1))
print(library.show_books())


















