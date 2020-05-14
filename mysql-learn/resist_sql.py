import mysql.connector

# 数据库的连接配置
config = {
  'host': '127.0.0.1',
  'port': 3306,
  'user': 'root',
  'password': '1q2w3e4r',
  'database': 'vega'
}

con = mysql.connector.connect(**config)

# sql注入的账号和密码
username = "1 OR 1=1"
password = "1 OR 1=1"
# sql = "SELECT COUNT(*) FROM t_user WHERE username="+username+" AND AES_DECRYPT(UNHEX(password),'fuck')="+password;

# cursor = con.cursor()
# cursor.execute(sql)
# print(cursor.fetchone())
# con.close()

# 预编译sql的方式来防止sql注入攻击
sql = "SELECT COUNT(*) FROM t_user WHERE username=%s AND AES_DECRYPT(UNHEX(password),'fuck')=%s";
cursor = con.cursor()
cursor.execute(sql, (username, password))
print(cursor.fetchone())
con.close()