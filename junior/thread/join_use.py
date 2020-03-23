import threading
import time


class Count(threading.Thread):
    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def run(self):
        print('开始执行进程数字为 ----- {}'.format(self.num))
        time.sleep(2)
        print('结束执行进程数字为 ***** {}'.format(self.num))


if __name__ == '__main__':
    print('主线程开始')
    c1 = Count(2)
    c2 = Count(3)
    c3 = Count(4)
    # print('c1 start')
    # c1.start()
    # c1.join()
    # print('c2 start')
    # c2.start()
    # c2.join()
    # print('c3 start')
    # c3.start()
    # c3.join()
    l = [c1, c2, c3]
    for i in l:
        print('线程开始执行')
        i.start()
    
    for i in l:
        print('线程开始阻塞')
        # 执行join方法之后 当前的进程之中的其他线程就会被阻塞
        i.join()
    
        
    print('主线程结束')
