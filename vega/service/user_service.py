from db.user_dao import UserDao

class User_service:
    __user_dao = UserDao()

    def login(self, username, password):
        return self.__user_dao.login(username, password)
    
    def get_user_role(self, username):
        return self.__user_dao.get_user_role(username)