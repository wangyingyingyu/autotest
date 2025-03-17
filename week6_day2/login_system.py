from flask import Flask, request, redirect, url_for

# 模拟数据库中的用户信息
users_db = {
    'feier': {
        'password': 'adminpass',
        'role': 'admin',
        # 状态包含已登陆 logged，未登录 unlogged
        'status': 'unlogged'
    },
    'lily': {
        'password': 'userpass',
        'role': 'user',
        'status': 'unlogged'
    }
}

app = Flask(__name__)

@app.route("/login")
def login():
    return "登录页面"
@app.route("/profile")
def profile(username):
    if users_db[username]["status"] != "logged":
        return redirect(url_for("login"))
    return "Welcome to {username}\'s Profile"

@app.route("/login",methods="POST")
def log_user():
    data = request.json
    # 验证请求数据是否包含用户名和用户密码
    if not data or "username" not in data or "password" not in data:
        return {
            "errcode":-1,
            "errmsg":"Error login data"
        }
    username = data["user_name"]
    password = data["password"]
    # 验证用户名是否存在
    if username not in users_db:
        return {
            "errcode":-1,
            "errmsg":"username not exists"
        }
    # 校验密码是否正确
    if password != users_db[username]["password"]:
        return {
            "errcode":-1,
            "errmsg":"password is incorrect"
        }
    # 用户标记为logged
    users_db[username]["status"] = "logged"
#   重定向到/dashboard路由
    return redirect(url_for("dashboard",username=username))

@app.route("/dashboard/<string:name>")
# 检查用户登录状态是否为logged
def check_log(name):
    if users_db[name]["status"] != "logged":
        return redirect(url_for("login"))
    if users_db[name]['role'] == "admin":
        return "Welcome to the Admin Dashboard"
    else:
        # 如果不是 admin，跳转到个人资料页
        return redirect(url_for('profile',username=name))

