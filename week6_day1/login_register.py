from flask import Flask,request
"""实战：用户注册与登录系统
开发一个简单的 Web 应用来处理用户注册和登录功能。用户通过前端发送用户名、密码等信息进行注册或登录，后端会根据请求处理数据并返回相应的响应信息。为了保证功能的正确性，需要配置测试环境，进行单元测试，验证系统是否正常工作。

- 用户注册： - 用户通过 POST 请求将用户名和密码提交到服务器进行注册。 
- 服务器会验证用户名是否已存在，如果已存在则返回一个错误信息。如果用户名有效且密码符合规则，则创建用户并返回注册成功的信息。 
- 用户登录： - 用户通过 POST 请求将用户名和密码提交到服务器进行登录。 
- 服务器会验证用户名和密码是否匹配，如果匹配，则返回登录成功的信息；如果不匹配，则返回错误信息。 
- 测试平台配置： - 配置测试环境，使用 pytest 测试用户注册和登录的接口是否正常工作，验证返回的状态码和响应内容。"""
user_list= {"a":"a12345",
            "b":"b12345"}

register = Flask(__name__)
@register.route("/register",methods=["POST"])
def register_info():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return {
                    "errcode": -1,
                    "errmsg": "Error user data",
                }
    else:
        user_name = data.get('username')
        pass_word = data.get('password')
        if user_name.isalnum() == True and pass_word.isalnum() == True:
            if user_name in user_list:
                return {
                    "errcode": -1,
                    "errmsg": "username already exists ",
                }
            else:
                if len(pass_word) == 6:
                    user_list[user_name] = pass_word
                    return {
                    "errcode": 0,
                    "message": "User registered successfully"
                }
                else:
                    return {
                    "errcode": -1,
                    "errmsg": "Password length is not enough",
                }
        else:
            return {
                    "errcode": -1,
                    "errmsg": "The user name or password format is incorrect",
                }


@register.route("/login",methods=["POST"])
def login_info():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return {
                    "errcode": -1,
                    "errmsg": "Error user data",
                }
    else:
        user_name = data.get('username')
        pass_word = data.get('password')
        if user_name.isalnum() == True and pass_word.isalnum() == True:
            if user_name in user_list:
                if len(pass_word) == 6:
                    if pass_word in user_list.values():
                        return {
                            "errcode": 0,
                            "message": "User login successfully"
                    }
                    else:
                        return {
                            "errcode": -1,
                            "errmsg": "Password not exists",
                        }
                else:
                    return {
                    "errcode": -1,
                    "errmsg": "Password length is incorrect",
                }
            else:
                return {
                    "errcode": -1,
                    "errmsg": "User not exists",
                }
        else:
            return {
                    "errcode": -1,
                    "errmsg": "The user name or password format is incorrect",
                }



if __name__ == '__main__':

    register.run(port=5051)




