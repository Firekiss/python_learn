from db.mysql_db import pool

class UserDao:
    # 用户登录
    def login(self, username, password):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT COUNT(*) FROM t_user WHERE username=%s AND AES_DECRYPT(UNHEX(password), 'fuck')=%s;"
            cursor.execute(sql, (username, password))
            ret = cursor.fetchone()[0]
            return True if ret == 1 else False
        except Exception as e:
            print('error ', e)
        finally:
            if 'con' in dir():
                con.close()

    # 获取用户权限
    def get_user_role(self, username):
        try:
            con = pool.get_connection()
            cursor = con.cursor()
            sql = "SELECT r.role FROM t_user u JOIN t_role r ON u.role_id = r.id WHERE u.username=%s;"
            cursor.execute(sql, (username,)) 
            return cursor.fetchone()[0]
        except Exception as e:
            print('error ', e)
        finally:
            if 'con' in dir():
                con.close()