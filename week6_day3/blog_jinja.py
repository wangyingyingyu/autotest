from flask import Flask, request, render_template
"""
实战：创建博客应用
创建一个博客应用，包含一个博客首页home page和博客详情页面。
首页展示所有博客文章的标题，详情页面展示文章的详细内容。
使用 Flask 模板技术动态渲染文章列表和文章详情页面。
假设文章数据是一个列表，每篇文章包含标题、作者和内容，使用模板循环渲染文章列表。
文章详情页面显示单个文章的标题、作者和正文内容。
"""
# 模拟的文章数据
posts = [
    {
        'id': 1,
        'title': 'Flask 入门',
        'author': 'Alice',
        'content': 'Flask 是一个轻量级的 Python Web 框架...'
    },
    {
        'id': 2,
        'title': 'Flask 模板技术',
        'author': 'Bob',
        'content': 'Flask 使用 Jinja2 模板引擎来渲染 HTML...'
    }
]
app = Flask(__name__)
@app.route("/blog")
def home_page():
    return render_template("blog_j.html",posts=posts)

@app.route("/blog/<int:id>")
def blog_post(id):
    for post in posts:
        if id == post["id"]:
            return render_template("post.html",post=post)
    else:
        # err = {
        #     "errcode": -1,
        #     "errmsg": "post_id not exists"
        # }
        #
        # return render_template("post.html",err=err)
        return {
            "errcode":-1,
            "errmsg":"post_id not exists"
        },404

if __name__ == '__main__':
    app.run(debug=True,port=5053)



