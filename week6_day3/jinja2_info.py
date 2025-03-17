# 创建一个简单的 Flask 应用，使用 Flask 模板技术渲染一个包含用户信息的页面。
# 页面包含用户的姓名和年龄，要求使用 Jinja2 模板语法将用户信息动态传递到 HTML 页面。
# 通过 URL 参数传递用户信息，例如 /user?name=John&age=30，并在模板中展示这些信息
# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route("/user/<name,age>")
# def user_info(name,age):
#     return render_template("jinja_info.html",name=name,age=age)
#
# if __name__ == "__main__":

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/user')
def user():
    name = request.args.get('name')
    age = request.args.get('age')

    return render_template('user.html', name=name, age=age)


if __name__ == '__main__':
    app.run(debug=True,port=5054)