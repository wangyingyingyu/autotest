# 先创建一个flask程序实例对象
from flask import Flask
app = Flask(__name__) # __name__是这个程序的模块名

# # 跟路由() “/” URL路径
# @app.route("/")
# # 视图函数
# def hello():
#     return "hello hogworts"

@app.route('/gets',methods=['GET'])
def get_in():
    return "methods == get"
# @app.route("/post",methods = ["post"])
# def post_info():
#     return "methods == post"
# @app.route("/put",methods=["put"])
# def put_info():
#     return "method == put"
# @app.route("/delete",methods=["DELETE"])
# def delete_info():
#     return "methods == delete"
# delete 请求
# @app.route("/delete", methods=["DELETE"])
# def delete():
#     return f"Method is DELETE."



# 运行应用程序
if __name__ == '__main__':
    app.run(port=5055)




