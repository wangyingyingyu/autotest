from flask import Flask
"""课堂练习
创建一个 Flask 应用，包含四个路由
分别对应 HTTP 请求方法（GET、POST、PUT、DELETE）。
每个路由只需返回一个简单的字符串响应，描述该请求方法的功能。
实战思路
创建一个简单的任务管理 API，支持以下操作：
GET 请求：返回任务列表。
POST 请求：创建一个新任务。
PUT 请求：更新任务的状态。
DELETE 请求：删除某个任务。
响应内容为字符串，描述操作成功。"""

app1 = Flask(__name__)

@app1.route("/tasks",methods=['GET'])
def get_info():
    return "获取任务列表"
@app1.route("/tasks",methods=["POST"])
def post_info():
    return "创建一个新任务"
@app1.route("/tasks/<int:task_id>",methods=["PUT"])
def put_info(task_id):
    return f'{task_id}更新'

@app1.route("/tasks/<int:task_id>",methods=["DELETE"])
def delete_info(task_id):
    return f'{task_id}删除'

if __name__ == '__main__':
    app1.run()

# 端口冲突  




