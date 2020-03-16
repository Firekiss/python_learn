

class Cat(object):
    def __init__(self):
        print('创建了cat对象 {}'.format(id(self)))

    def __del__(self):
        print('垃圾回收cat对象 {}'.format(id(self)))
    

def f0():
    while True:
        c = Cat()

if __name__ == '__main__':
    """
    当创建的变量被垃圾回收器 检测到引用次数为0的时候，就会被回收
    当检测到被引用的次数不为0的时候就从这一代升级到下一代的引用对象
    """
    f0()