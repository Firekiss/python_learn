import redis
from redis_db import pool

con = redis.Redis(connection_pool = pool)
empnos = con.smembers("empno")
print(empnos)
del con

