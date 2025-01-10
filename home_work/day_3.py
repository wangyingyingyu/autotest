"""课后作业
- 创建一个包含员工信息的管理系统，员工的信息包括 姓名（字符串）、月考勤天数（列表，每月天数） 和 额外信息（字典，存储例如职位和联系方式）。
- 添加新员工：向系统中添加一个新员工的所有信息（包括姓名、考勤天数和额外信息）。
- 更新员工考勤：修改指定员工某个月的考勤天数。
- 删除员工信息：从系统中删除某个员工的信息。
- 获取员工列表：输出所有员工的姓名。
- 查找员工信息：通过姓名查找并输出该员工的完整信息。"""

# employees = {
#     "小明":{"name":"小明","days":30, "telephone":1123},
#     "奇奇":{"name":"奇奇","days":29, "telephone":1120},
#     "Eve":{"name":"Eve","days":31, "telephone":1234}
#
# }

employees = {
    "John": {
        # 一个季度的考勤天数
        "attendance": [20, 22, 19],
        # 附加信息
        "extra_info": {
            # 职位
            "position": "Manager",
            # 联系方式
            "contact": "13012345678"
        }
    }
}
# 添加新员工
employees["Tom"] = ({"attendance": [21, 22, 20],"extra_info": {"position": "assisant","contact": "13012345990"}})
print(f'添加新员工后的管理系统{employees}')

# 更新员工考勤
work_days = [22,21,21]
staff = "John"

if staff in employees:
    employees[staff]["attendance"] = work_days
    print(f'员工{staff}的月考勤天数已更新为{work_days}天')
else:
    print(f'员工{staff}不存在')
print(f'修改后的员工系统为{employees}')

# 删除员工信息
staff_02 = "Tom"
if staff_02 in employees:
    del employees[staff_02]
    print(f'员工{staff_02}信息已删除')
else:
    print(f'员工{staff_02}不存在')
print(f'修改后的员工系统为{employees}')

# 获取员工列表
print(f'全体员工列表为{employees.keys()}')

# 查找员工信息
staff_03 = "John"
if staff_03 in employees:
    print(f"员工 '{staff_03}' 的信息是：{employees[staff_03]}")
else:
    print(f"学生 '{staff_03}' 不存在于字典中。")





