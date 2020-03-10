"""
使用迭代器和生成器模拟原生的rang方法
"""

class MeRange(object):
    """
    使用迭代器实现rang方法
    """
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start == self.end - 1:
            raise StopIteration
        self.start += 1
        return self.start


class MeGenerator(object):
    """
    使用生成器实现range
    """
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    # 这个函数的真正执行在第一次调用next()函数的时候才会执行
    def get_number(self):
        while True:
            if self.start >= self.end:
                break
            self.start += 1
            yield self.start


if __name__ == '__main__':
    # me = MeRange(2, 10)
    # for i in me:
    #     print(i)
    me_ge = MeGenerator(3, 9).get_number()
    # print(list(me_ge))
    # for i in me_ge:
    #     print(i)
