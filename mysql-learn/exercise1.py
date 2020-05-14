import mysql.connector.pooling

config = {
  'host': '127.0.0.1',
  'port': 3306,
  'user': 'root',
  'password': '1q2w3e4r',
  'database': 'demo'
}

try:
  pool = mysql.connector.pooling.MySQLConnectionPool( 
    pool_size=10,
    **config
  )

  con = pool.get_connection()  #从连接池子里面捞一个连接使用
  con.start_transaction()
  cursor = con.cursor()  #创建游标

  sql = "DROP TABLE t_emp_new;"  #删除数据表
  # cursor.execute(sql)
  sql = "CREATE TABLE t_emp_new LIKE t_emp;"  #新建数据表
  cursor.execute(sql)
  sql = "SELECT AVG(sal) FROM t_emp;"  #查询公司的平均工资
  cursor.execute(sql)
  avg_sal = cursor.fetchone()[0]
  print('公司平均工资 %f' % avg_sal)
  sql = "SELECT deptno FROM t_emp GROUP BY deptno HAVING AVG(sal) >= %s;"
  cursor.execute(sql, (avg_sal,))
  deptnos = []
  for deptno in cursor:
    deptnos.append(deptno[0])
  sql = "INSERT INTO t_emp_new SELECT * FROM t_emp WHERE deptno in ("
  for i in range(len(deptnos)):
    if i < len(deptnos) - 1:
      sql = sql + str(deptnos[i]) + ','
    else:
      sql = sql + str(deptnos[i])
  sql = sql + ");"
  cursor.execute(sql)
  sql = "DELETE FROM t_emp WHERE deptno in ("
  for i in range(len(deptnos)):
    if i < len(deptnos) - 1:
      sql = sql + str(deptnos[i]) + ','
    else:
      sql = sql + str(deptnos[i])
  sql = sql + ");"
  cursor.execute(sql)
  sql = "SELECT deptno FROM t_dept WHERE dname='SALES';"
  cursor.execute(sql)
  sales_deptno = cursor.fetchone()[0]
  sql = "UPDATE t_emp_new SET deptno = %s;"
  cursor.execute(sql, (sales_deptno,))
  con.commit()
except Exception as e:
  if 'con' in dir():
    con.rollback()
