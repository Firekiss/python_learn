# 使用多线程进行内容的读写

from multiprocessing import Process, Queue
import time

class ReadProcess(Process):
    def __init__(self, q, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = q


    def run(self):
        l = [
            '锄禾日当午',
            '汗滴禾下土',
            '谁知盘中餐',
            '粒粒皆辛苦'
        ]
         
        for line in l:
            self.q.put(line)
            print('read process put line in queue: {}'.format(line))
            time.sleep(2)


class WriteProcess(Process):
    def __init__(self, q, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.q = q

    
    def run(self):
        while True:
            line = self.q.get()
            print('write process get line in queue: {} '.format(line))


if __name__ == '__main__':
    q = Queue(10)
    r = ReadProcess(q)
    w = WriteProcess(q)
    r.start()
    w.start()