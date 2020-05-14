import redis
from redis_db import pool

try:
    con=redis.Redis(connection_pool=pool)  # 获取到连接
    file=open(file='./student.txt', mode='r', encoding='utf-8')
    lines = file.read().splitlines()
    for line in lines:
        infos = line.split(',')
        id = infos[0]
        name = infos[1]
        class_name = infos[2]
        grade_1 = float(infos[3])
        grade_2 = float(infos[4])
        grade_3 = float(infos[5])
        if grade_1 >= 80 and grade_2 >= 80 and grade_3 >= 80:
            con.hmset(id, {"grade_1": grade_1, "grade_2": grade_2, "grade_3": grade_3})
    print("三门成绩都大于85分的学生信息写入成功")
except Exception as e:
    print("error is : ", e)
finally:
    if "con" in dir():
        del con
