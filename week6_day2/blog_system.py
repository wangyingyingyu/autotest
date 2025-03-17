from flask import Flask, Blueprint,request

"""
实战：简易博客系统
使用 Flask 的蓝图机制来组织不同的功能模块：
auth_blueprint：处理用户身份验证（注册、登录）。
post_blueprint：处理博客文章的创建、查询和删除功能。
每个蓝图中定义不同的视图（视图函数）：
auth_blueprint：
用户注册视图（/register）。
用户登录视图（/login）。
post_blueprint：
创建博客文章视图（/posts/create）。
查看所有文章视图（/posts）。
查看某一篇文章视图（/posts/）。
删除博客文章视图（/posts/delete）"""
app6 = Flask(__name__)
# 创建蓝图对象           蓝图名称         蓝图所在模块   定义URL前缀，定义蓝图对象路由时自动调用这个URL前缀
auth_blueprint = Blueprint(name="user", import_name=__name__, url_prefix="/auth")
# 使用蓝图对象定义路由
user_list= {"a":"a12345",
            "b":"b12345"}
@auth_blueprint.route("/register", methods=["POST"])
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


@auth_blueprint.route("/login", methods=["POST"])
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
                            "errmsg": "Password is incorrect",
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
# post_blueprint：
# 创建博客文章视图（/posts/create）。
# 查看所有文章视图（/posts）。
# 查看某一篇文章视图（/posts/）。
# 删除博客文章视图（/posts/delete）


# 简单用户数据存储
# {"username": "password"}
# 简单博客数据存储
post_dict = {"1": {"post_title": "a", "content": "aaa"}}

post_blueprint = Blueprint(name="post",import_name=__name__,url_prefix="/posts")
@post_blueprint.route("/create",methods=["POST"])
    # 创建文章视图
def create_post():
    data = request.json
    # 校验请求数据
    if not data or "post_title" not in data or "content" not in data:
        return {
                    "errcode": -1,
                    "errmsg": "Error post data",
                },400
    post_title = data.get("post_title")
    post_content = data.get("content")
    # 查看博客题目是否已经存在
    #
    for i in post_dict.values():

        if post_title == i["post_title"]:
            return {
                        "errcode": -1,
                        "errmsg": "post_name already exists",
                    }
    else:
        post_data = {}
        post_data["post_title"] = post_title
        post_data["content"] = post_content

        post_id = int(max(list(post_dict.keys()))) + 1
        post_dict[str(post_id)] = post_data

        return {
            "errcode": 0,
            "errmsg": "Create a blog successfully",
        }
# 查看某一篇文章视图
@post_blueprint.route("/<int:posts_id>",methods=["POST"])

def post_view(posts_id):
    post_id = str(posts_id)
    if post_id in post_dict.keys():
        return {
            "errcode":0,
            "post_title":post_dict[post_id]["post_title"],
            "post_content":post_dict[post_id]["content"]
        }
    else:
        return {
            "errcode":-1,
            "errmsg":"post_id not exists"
        }

# 查看所有的文章视图
@post_blueprint.route("",methods=["GET"])
def post_all():
    post_info = [{"post_id:":post_id,"post_title:":{post["post_title"]},"post_content:":{post["content"]}}
                 for post_id,post in post_dict.items()]
    return {
        "errcode": 0,
        "message": "Get posts successfully",
        "tasks": post_info
    }

# 删除博客
@post_blueprint.route("/delete/<int>:post_id",methods=["DELETE"])

def post_delete(post_id):
    if str(post_id) in post_dict.keys():
        del post_dict[str(post_id)]
        return {
            "errcode":0,
            "errmsg": "Post deleted success"

        }
    else:
        return {
            "errcode":-1,
            "errmsg":"post_id not exists"
        }

if __name__ == '__main__':
    # 注册蓝图到应用
    app6.register_blueprint(auth_blueprint)
    app6.register_blueprint(post_blueprint)
    app6.run(debug=True,port=5052)










