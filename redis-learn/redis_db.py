import redis

# 创建连接池
pool = redis.ConnectionPool(
    host = "localhost",
    port = 6379,
    password = "1q2w3e4r",
    db = 0,
    max_connections = 200
)