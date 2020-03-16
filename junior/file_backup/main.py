"""
文件目录下文件资源备份
"""

import os
import os.path


class BackUpFiles(object):
    def __init__(self, src, dist):
        self.src = src
        self.dist = dist

    def analyze_dist_dir(self):
        # 解析目标文件夹是否存在 如果不存在 则创建目标文件夹
        print('开始解析目标文件夹')
        if not os.path.exists(self.dist):
            print('目标文件夹不存在, 创建目标文件夹')
            os.mkdir(self.dist)

    def backup_file(self, file_path):
        basename = os.path.basename(file_path)
        tar_path = os.path.join(self.dist, basename)
        with open(tar_path, 'w', encoding='utf-8') as wf, open(file_path, 'r', encoding='utf-8') as rf:
            while True: 
                ret = rf.read(100)
                if not ret:
                    break
                wf.write(ret)
            wf.flush()
            print('文件 {} 已经备份完毕!'.format(basename))

    def backup(self):
        # 进行备份的函数
        print('开始进行备份...')
        self.analyze_dist_dir()
        print('开始解析备份文件夹下面的文件')
        file_list = os.listdir(self.src)
        for file in file_list:
            file_path = os.path.join(self.src, file)
            if not os.path.isfile(file_path):
                print('当前解析对象为文件夹, 不进行备份')
            else:
                print('开始对文件 {} 进行备份'.format(file))
                self.backup_file(file_path)


if __name__ == '__main__':
    # 获取当前执行文件的绝对路径
    abs_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(abs_path)
    print('当前执行文件的文件夹路径 > {}'.format(dir_path))
    src_path = os.path.join(dir_path, 'src')
    target_path = os.path.join(dir_path, 'dist')
    # 实例化备份对象
    backup_files = BackUpFiles(src_path, target_path)
    backup_files.backup()
    