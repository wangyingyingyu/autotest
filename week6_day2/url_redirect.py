from flask import Flask, Blueprint, redirect, url_for

"""课堂练习：基本的路由跳转
创建一个包含 /home 和 /dashboard 路由的 Flask 应用。
使用普通路由定义方式。
在 /home/user 路由中携带访问者用户名，如果访问者在 users_list 列表中，代表已经登录，跳转到 /dashboard。 
- /dashboard 返回提示信息 Welcome to the Dashboard。
如果访问者未满足条件，应该跳转到 /login 路由。 - /login 返回提示信息 'Please log in'"""
users_list = ["a","b"]
app = Flask(__name__)

index = Blueprint("index",__name__)
log = Blueprint("login",__name__)

@index.route("/dashboard")
def dash():
    return "Welcome to the Dashboard"
@log.route("/login")
def log_in():
    return "Please log in"

@index.route("/user/<user_name>",methods=["GET"])
def user(user_name):
    if user_name in users_list:
        print("登录，成功后跳转到首页")
        return redirect(url_for("index.dash"))
    else:
        print("登录失败")
        return redirect(url_for("login.login"))

if __name__ == '__main__':
    app.register_blueprint(index)
    app.register_blueprint(log)
    app.run(debug=True,port=5055)
