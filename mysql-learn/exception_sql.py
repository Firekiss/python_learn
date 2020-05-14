import mysql.connector

config={
  'host': '127.0.0.1',
  'port': 3306,
  'user': 'root',
  'password': '1q2w3e4r',
  'database': 'vega'
}

try:
  con = mysql.connector.connect(**config)
  # 开始事务
  con.start_transaction()
  cursor = con.cursor()
  sql = "SELECT * FROM t_user"
  cursor.execute(sql)
  print(cursor.fetchall())
  con.commit()
except Exception as e:
  if "con" in dir():
    con.rollback()
  print('err', e)
finally:
  if "con" in dir():
    con.close()