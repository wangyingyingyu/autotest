# 使用 Flask 创建一个应用，实现一个登录接口，接收用户名和密码，
# 如果用户名是 "admin" 且密码是 "1234"，返回欢迎信息，否则返回错误信息
from flask import Flask,request
app = Flask(__name__)

@app.route("/login",methods=["POST"])
def login():
    data=request.json
    if not data or "name" not in data or "password" not in data:
        return {
            "errcode":-1,
            "errmsg":"data is incorrect"
        }
    user_name=data.get("name")
    if user_name != "admin":
        return {
            "errcode": -1,
            "errmsg": "username is incorrect"
        }
    password = data.get("password")
    if password != "1234":
        return {
            "errcode": -1,
            "errmsg": "password is incorrect"
        }
    return {
        "errcode": 0,
        "errmsg": "login successfully"
    }
if __name__ == "__main__":
    app.run(debug=True,port=5054)

