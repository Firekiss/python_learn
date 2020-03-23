from multiprocessing import Process, Queue
import time

def f(q):
    # 向列队之中添加列表
    q.put([42, None, 'hello'])


if __name__ == '__main__':
    # 实例化一个列队
    q = Queue()
    # 实例化进程
    p = Process(target=f, args=(q,))
    p.start()
    # 当列队里面没有内容的时候，会阻塞不执行下面的代码
    print(q.get())
    p.join()