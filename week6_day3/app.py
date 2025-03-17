from flask import Flask, request, render_template

app = Flask(__name__)

users_db = {
    "feier": "123456"
}

@app.route("/")
def index():
    return render_template("demo.html")

# 登录路由
@app.route('/login', methods=['POST'])
def login():
    data = request.form
    # 校验请求数据中是否包含 username 与 password
    if not data or "username" not in data or "password" not in data:
        # 如果不包含，返回错误提示信息
        return {
           "errcode": -1,
           "errmsg": "Error user data",
        }, 400
    username = data.get('username')
    password = data.get('password')

    # 检查用户名是否存在
    if username not in users_db:
        return {
            "errcode": -1,
            "message": "User not found"
        }

    # 检查用户名和密码是否匹配
    if users_db[username] != password:
        return {
            "errcode": -1,
            "message": "Incorrect password"
        }

    return {
        "errcode": 0,
        "message": "Login successful"
    }


if __name__ == '__main__':
    app.run(debug=True)