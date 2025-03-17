# 课堂练习
# 创建一个简单的 Flask 应用，展示如何使用 Flask 提供的静态文件功能。
# 在 static 文件夹中放置一个 CSS 文件，并在 HTML 模板中引用该文件来为页面添加样式。
# 页面展示一个标题，要求使用该 CSS 文件来修改标题的颜色和字体大小。
# 静态文件存放在 static 文件夹中，CSS 文件命名为 style.css。

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('static_css.html')

if __name__ == '__main__':
    app.run(debug=True)