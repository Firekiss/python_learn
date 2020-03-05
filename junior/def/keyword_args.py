def info(*, desc, birth, name='imooc'):
    print('{name}-{desc}出生于{birth}'.format(name=name, desc=desc, birth=birth))


info(desc='程序员的梦工厂', birth='2013年8月')