import threading

def loop():
    n = 0
    while n < 5:
        print('current thead name is {}'.format(threading.current_thread().name))
        print('当前循环的数字是 : {}'.format(n))
        n += 1



if __name__ == '__main__':
    print('current thead name is {}'.format(threading.current_thread().name))
    t = threading.Thread(target=loop, name='loop thread')
    t.start()
    t.join()
