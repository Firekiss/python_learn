import os
import time
from multiprocessing import Process


def me_process(process_name):
    time.sleep(3)
    print('current process name is : {} **** pid is {}'.format(process_name, os.getpid()))


class MeProcess(Process):
    
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.process_name = name

    def run(self):
        time.sleep(3)
        print('current process name is : {} **** pid is {}'.format(self.process_name, os.getpid()))


if __name__ == '__main__':
    # p = Process(target=me_process, args=('me_process',))
    # p.start()
    # p.join()
    
    mp = MeProcess('fuck process')
    mp.start()
    mp.join()
    print('进程执行完毕')



