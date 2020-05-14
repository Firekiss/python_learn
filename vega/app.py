import os, sys, time
from getpass import getpass
from colorama import Fore,Style
from service.user_service import User_service

__user_service = User_service()

def main():
    while True:
        os.system("clear")
        print(Fore.LIGHTBLUE_EX, "\n\t=====================")
        print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
        print(Fore.LIGHTBLUE_EX, "\n\t=====================")
        print(Fore.LIGHTGREEN_EX, "\n\t1.登陆系统")
        print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
        print(Style.RESET_ALL)
        opt = input("\n\t输入操作编号: ")
        if opt == '1':
            username = input("\n\t用户名:")
            password = getpass("\n\t用户密码:")
            ret = __user_service.login(username, password)
            if ret == True:
                role = __user_service.get_user_role(username)
                os.system("clear")
                while True:
                    if role == "管理员":
                        print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                        print(Fore.LIGHTGREEN_EX, "\n\t2.人员管理")
                        print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                        print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                        print(Style.RESET_ALL)
                        opt = input("\n\t输入操作编号:")
                        if opt == "back":
                            break
                        elif opt == "exit":
                            sys.exit(0)
                        
                    elif role == "新闻编辑":
                        pass
            else:
                print("\n\t登录失败(3秒后自动fanhui )")
                time.sleep(3)
        elif opt == '2':  # 点击了退出系统
            sys.exit(0)
        


if __name__ == '__main__':
    main()