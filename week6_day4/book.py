from flask import Flask, render_template

app = Flask(__name__)

# 模拟的书籍数据
books = [
    {
        'id': 1,
        'title': 'Python编程快速上手',
        'author': 'Eric Matthes',
        'cover': 'python_cover.png',
        'description': '一本适合初学者的 Python 编程书籍。'
    },
    {
        'id': 2,
        'title': '深入浅出设计模式',
        'author': 'Erich Gamma',
        'cover': 'design_patterns_cover.png',
        'description': '经典的设计模式教程，帮助你提高编程思维。'
    }
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return render_template('book_detail.html', book=book)
    else:
        return "Book not found", 404

if __name__ == '__main__':
    app.run(debug=True,port=5054)