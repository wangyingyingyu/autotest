from flask import Flask, Blueprint,request

"""
课堂练习
创建一个 Flask 项目，使用蓝图（Blueprint）组织不同的功能模块。
定义两个蓝图：
user_blueprint：处理用户相关功能，如注册、登录。
task_blueprint：处理任务相关功能，如创建任务、查看任务。
每个蓝图中定义不同的视图（视图函数）：
user_blueprint：
注册视图（/register）。
登录视图（/login）。
"""
# 创建APPflask实例对象
app5 = Flask(__name__)
# 创建蓝图实例对象
user_blueprint = Blueprint("user_blueprint",__name__,url_prefix="/blueprint")
user_list= {"a":"a12345",
            "b":"b12345"}
#创建蓝图对象路由信息
@user_blueprint.route("/register",methods=["POST"])
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


@user_blueprint.route("/login",methods=["POST"])
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


# task_blueprint：
# 创建任务视图（/tasks/create）。
# 查看任务视图（/tasks）。
# 查看任务详情视图（/tasks/）。
# 简单用户数据存储
# {"username": "password"}
# 简单任务数据存储
task_dict = {"1": {"task_name": "a", "content": "aaa"}}
# 创建蓝图对象
task_blueprint = Blueprint("task_blueprint",__name__,url_prefix="/blueprint/tasks")
# 创建任务视图
@task_blueprint.route("/create",methods=["POST"])
def task_create():
    data = request.json
    if not data:
        # 如果不包含，返回错误提示信息
        return {
            "errcode": -1,
            "errmsg": "Error post data",
        }, 400

    task_id = list(data.keys())[0]
    task_info = data[task_id]
    if  task_dict:
        if task_id in task_dict:
            return {
                        "errcode": -1,
                        "errmsg": "Task already exists",
                    }
        else:
            task_dict[task_id] = task_info
            return {
                        "errcode": 0,
                        "errmsg": "Task creation succeeded",
                    }
    else:
        return {
            "errcode": -1,
            "errmsg": "The task dictionary does not exist",
        }

# 查看任务视图（/tasks）
@task_blueprint.route("/view",methods=["POST"])
def task_view():
    data = request.json
    if not data or "task_id" not in data:
        # 如果不包含，返回错误提示信息
        return {
            "errcode": -1,
            "errmsg": "Error post data",
        }, 400
    task_id = data["task_id"]

    if  task_dict:
        if task_id in task_dict.keys():
            print(task_dict[task_id])
            return task_dict[task_id]
        else:
            return {
                        "errcode": -1,
                        "errmsg": "Task does not exist",
                    }
    else:
        return {
            "errcode": -1,
            "errmsg": "The task dictionary does not exist",
        }
# 查看任务详情视图（/tasks/
#task_dict = {"1": {"task_name": "a", "content": "aaa"}}
@task_blueprint.route("/d",methods=["POST"])
def task_detail():
    data = request.json
    if not data or "task_id" not in data:
        # 如果不包含，返回错误提示信息
        return {
            "errcode": -1,
            "errmsg": "Error post data",
        }, 400
    task_id = data["task_id"]
    if task_dict:
        if task_id in task_dict.keys():
            print(f'任务名称为：{task_dict[task_id]["task_name"]},任务内容为：{task_dict[task_id]["content"]}')
            return {
                "errcode": 0,
                "errmsg": "Task's detail success",
                "task_name": task_dict[task_id]["task_name"],
                "content": task_dict[task_id]["content"]
            }
        else:
            return {
                "errcode": -1,
                "errmsg": "Task does not exist",
            }
    else:
        return {
            "errcode": -1,
            "errmsg": "The task dictionary does not exist",
        }


if __name__ == '__main__':
    # 蓝图注册到 flask 启动对象中。
    app5.register_blueprint(user_blueprint)
    app5.register_blueprint(task_blueprint)
    app5.run(port=5051)







