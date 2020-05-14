from mysql.connector.pooling import MySQLConnectionPool

# 数据库连接配置
__config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '1q2w3e4r',
    'database': 'vega'
}

try:
    pool = MySQLConnectionPool(
        pool_size = 10,
        **__config
    )
except Exception as e:
    print('创建数据库连接池失败 ', e)