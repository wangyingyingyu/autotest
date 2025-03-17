# 编写一个简单的 Flask 应用，渲染一个 HTML 模板，模板中显示一个动态传递的用户名。

from flask import Flask,render_template
app = Flask(__name__)
@app.route("/index")
def index():
    name="Tom"
    return render_template("demo.html",name=name)


if __name__ == "__main__":
    app.run(debug=True,port=5054)