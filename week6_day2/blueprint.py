from flask import Flask
from flask.sansio.blueprints import Blueprint

app4 = Flask(__name__)
# 定义蓝图的对象
user_bp = Blueprint(name="user",import_name=__name__)

#使用route装饰器定义蓝图
# 将蓝图对象注册到app4应用中
# 定义添加前缀的蓝图对象