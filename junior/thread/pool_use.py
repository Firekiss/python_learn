import time
import threading
from concurrent.futures import ThreadPoolExecutor


apply_time = 10


def print_num(num):
    time.sleep(2)
    print('***** my thread is {}, my num is {} *****', threading.current_thread().name, num)

# 通常的使用主线程跑的方式
def usually_apply():
    for i in range(apply_time):
        print_num(i)


# 使用多线程的方式
def thread_apply():
    tasks = []
    for i in range(apply_time):
        task = threading.Thread(target=print_num, args=(i,))
        tasks.append(task)
    
    for task in tasks:
        task.start()
    
    for task in tasks:
        task.join()


# 使用线程池的方式
def thread_pool_apply():
    with ThreadPoolExecutor(max_workers=10) as pool:
        for i in range(apply_time):
            pool.submit(print_num, i)



if __name__ == '__main__':
    start_time = time.time()
    # usually_apply()
    # thread_apply()
    thread_pool_apply()
    end_time = time.time()
    print('total apply time is : ', end_time - start_time)