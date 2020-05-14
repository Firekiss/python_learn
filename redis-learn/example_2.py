import redis
from redis_db import pool

try:
    con = redis.Redis(connection_pool=pool)
    con.hmset("manager", {"name": "alex", "age": 30, "sex": "male"})
    con.hset("manager", "country", "china")
    con.hdel("manager", "sex")
    has_keys = con.exists("manager", "country", "age")
    print(has_keys)
    infos = con.hgetall("manager")
    print(infos)
    for one in infos:
        print(one.decode("utf-8"), infos[one].decode("utf-8"))
except Exception as e:
    print("error is : ", e)
finally:
    if 'con' in dir():
        del con