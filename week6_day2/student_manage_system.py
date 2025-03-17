from flask import Flask, Blueprint, request

class Student:

    def __init__(self, sid, name, age, gender):
        self.sid = sid
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"SID: {self.sid} Name: {self.name} Age: {self.age} Gender: {self.gender}"

    def to_dict(self):
        return {
            "sid": self.sid,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

students_db = {}

# 创建 Flask 应用对象
app = Flask(__name__)

# 创建学生管理蓝图
student_bp = Blueprint('student', __name__, url_prefix="/students")

@student_bp.route("/add", methods=["POST"])
def add_student():
 #{"sid": sid, "name": name, "age": age, "gender": gender}
    data = request.json
    if not data or "sid" not in data or "name" not in data:
        return {
           "errcode": -1,
           "errmsg": "Error student data",
        }, 400

    # 必填参数
    sid = data.get("sid")
    if sid in students_db:
        return {
           "errcode": -1,
           "errmsg": "Student id already exists",
        }
    name = data.get("name")
    if "age" in data:
        age = data.get("age")
    else:
        age = None
    if "gender" in data:
        gender = data.get("gender")
    else:
        gender = None
    # 获取学生实例
    stu = Student(sid, name, age, gender)
    # 添加学生实例，使用学生 id 作为 key
    students_db[sid] = stu
    return {
        "errcode": 0,
        "message": "Student create successful",
        "datas": stu.to_dict()
    }

@student_bp.route("/list")
def students_list():
    stu_list = [stu.to_dict() for stu in students_db.values()]
    return {
        "errcode": 0,
        "message": "Student list get successful",
        "datas": stu_list
    }
# 通过学号查询学生信息
@student_bp.route("/query/<string:sid>")
def get_student(sid):
    if sid not in students_db:
        return {
           "errcode": -1,
           "message": "Student not found"
        }, 404
    stu = students_db.get(sid)
    return {
        "errcode": 0,
        "message": "Student list get successful",
        "datas": stu.to_dict()
    }

@student_bp.route("/update/<string:sid>", methods=["PUT"])
def update_student(sid):
    if sid not in students_db:
        return {
           "errcode": -1,
           "message": "Student not found"
        }, 404
    # json 格式 {"name": name, "age": age, "gender": gender}
    data = request.json
    if not data or "name" not in data or "age" not in data or "gender" not in data:

        return {
           "errcode": -1,
           "errmsg": "Error student data",
        }, 400
    # 获取请求中的数据
    name = data.get("name")
    age = data.get("age")
    gender = data.get("gender")
    # 修改系统中的值
    stu = students_db[sid]
    stu.name = name
    stu.age = age
    stu.gender = gender
    return {
        "errcode": 0,
        "message": "Student update successful",
        "datas": stu.to_dict()
    }

@student_bp.route("/delete/<string:sid>", methods=["DELETE"])
def delete_student(sid):
    if sid not in students_db:
        return {
           "errcode": -1,
           "message": "Student not found"
        }, 404
    del students_db[sid]
    return {
        "errcode": 0,
        "errmsg": "Student deleted successful",
        "datas": {
            "sid": sid
        }
    }

if __name__ == '__main__':
    app.register_blueprint(student_bp)
    app.run(debug=True,port=5059)
