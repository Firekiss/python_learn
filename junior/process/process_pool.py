from multiprocessing import Process, Pool, current_process
import time


def run(num):
    print('pid is {0}, num is {1}'.format(current_process().pid, num))
    time.sleep(2)
    

if __name__ == '__main__':
    pool = Pool(2)
    for i in range(10):
        pool.apply_async(run, args=(i,))    
    pool.close()
    pool.join()
    print('finish!')

