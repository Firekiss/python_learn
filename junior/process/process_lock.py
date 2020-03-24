from multiprocessing import Process, Lock
import time, random 


# 创建进程互斥锁
lock = Lock()


class WriteProcess(Process):

    def __init__(self, process_num, lock, *args, **kwargs):
        self.process_num = process_num
        self.lock = lock
        super().__init__(*args, **kwargs )
 

    def run(self):
        with self.lock:
            for i in range(5):
                with open('file.txt', 'a', encoding='utf-8') as f:
                    write_con = 'pid is : {0}, process_name is {1}, process_num is {2} \n'.format(self.pid, self.name, self.process_num)
                    print(write_con)
                    f.write(write_con)
                    time.sleep(random.randint(2, 5))
    

if __name__ == '__main__':  
    for i in range(5):
        wp = WriteProcess(i, lock)
        wp.start()
