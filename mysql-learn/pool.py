import mysql.connector.pooling

config = {
  'host': '127.0.0.1',
  'port': 3306,
  'user': 'root',
  'password': '1q2w3e4r',
  'database': 'demo'
}

# 使用连接池进行数据插入
try:
  pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_size=10,
    **config
  )
  con = pool.get_connection()
  con.start_transaction()
  cursor = con.cursor()
  sql = "INSERT INTO t_emp (empno,ename,job,mgr,hiredate,sal,comm,deptno) VALUES (8000,'TONY','CLERK',7934,'1988-08-08',1000,200,10);"
  cursor.execute(sql)
  con.commit()
except Exception as e:
  if 'con' in dir():
    con.rollback()
  print('e >>> ', e)