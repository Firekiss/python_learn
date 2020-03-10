"""
带参数的装饰器
"""


def log(name=None):
    def decorate(func):
        def wrap(*args, **kwargs):
            print('{}.start...'.format(name))
            ret = func(*args, **kwargs)
            print('{}.end...'.format(name))
            return ret
        return wrap
    return decorate

@log('add')
def add(a, b):
    return a + b


if __name__ == '__main__':
    ret = add(4, 5)
    print(ret)