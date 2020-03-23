import threading
import time

lock = threading.Lock()
global_num = 0

class Count(threading.Thread):
    """
    计数器线程类
    """

    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def run(self):
        global global_num
        for i in range(10000):
            try:
                lock.acquire()
                global_num += self.num
                time.sleep(1)
                global_num -= self.num
                print('*' * 20)
                print('当前的全景数据修改结果为 {}'.format(global_num))
            finally:
                lock.release()
                

if __name__ == '__main__':
    c1 = Count(5)
    c2 = Count(8)
    c1.start()
    c2.start()
    c1.join()
    c2.join()

