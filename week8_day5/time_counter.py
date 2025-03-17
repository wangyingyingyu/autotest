# 1. 写 SQL 查询成绩⼩于 60 分的所有学⽣名单
# 1. 请写出⼀个 SQL 语句来查询分数前 5 的所有⼈
# 1. ⽤ SQL 得出每个部⻔的平均⼯资：对于员⼯表(employees)的 部⻔编号字段(department_id)与 部⻔表 (departments)的 主键字段(id) 有关联。
# 1. 设计支付场景的测试用例。
# 5. 编写一个计时的装饰器。
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"函数 {func.__name__} 执行时间: {run_time:.4f} 秒")
        return result
    return wrapper


@time_decorator
def example_function():
    time.sleep(3)  # 模拟一个耗时操作
    return "完成"

example_function()