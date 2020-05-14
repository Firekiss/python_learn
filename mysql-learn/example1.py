import mysql.connector

con = mysql.connector.connect(
  host="localhost",
  port="3306",
  user="root",
  password="1q2w3e4r",
  database="vega"
)

cursor=con.cursor()
sql="SELECT id,username,email,role_id FROM t_user"
cursor.execute(sql)

for one in cursor:
  print(one)

con.close()