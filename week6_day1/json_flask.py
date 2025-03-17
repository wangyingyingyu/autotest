from flask import Flask,request

"""课堂练习
创建一个简单的 Flask 应用，设置一个 POST 路由来处理请求数据。
在请求中发送 JSON 数据，并在 Flask 中接收该数据并返回一个响应，内容是处理后的数据。"""
app2 = Flask(__name__)

json = {
    "name":"xiaoming",
    "action":'post json'
}
@app2.route("/json",methods=["POST"])
def json_post():
    #
    data = request.json
    print(data)
    name = data.get('name')
    action = data.get('action')

    return name,action
if __name__ == '__main__':
    app2.run(port=5056)