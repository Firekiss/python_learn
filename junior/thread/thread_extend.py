import threading


class Loop(threading.Thread):
    n = 1

    def run(self):
        while self.n < 5:
            thread_name = threading.current_thread().name
            print('current thread name is {}'.format(thread_name))
            print(self.n)
            self.n += 1

if __name__ == '__main__':
    print('current thread name is {}'.format(threading.current_thread().name))
    loop = Loop(name='Loop Thread')
    loop.start()
    loop.join()

