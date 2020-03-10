"""
迭代器
"""

class Power(object):
    def __init__(self):
        self.__val = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__val += 1
        if self.__val > 10:
            raise StopIteration
        return self.__val * self.__val


if __name__ == '__main__':
    p = Power()
    for i in p:
        print(i) 
        
