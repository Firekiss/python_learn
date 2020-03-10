"""
装饰器的基础使用
"""


def log(func):
    def wrap():
        print('开始执行函数')
        func()
        print('结束执行函数')
    return wrap

def log_in(func):
    def wrap():
        print('start...')
        func()
        print('end...')
    return wrap

@log
@log_in
def hello():
    print('hello world')


if __name__ == '__main__':
    hello()