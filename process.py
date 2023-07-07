from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('同步进程差不多，从而又叫同步进程')
    print('完� overcome the file [%s] in process [%d]' % (filename, getpid()))
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('下載完戶 [%s]，耗蓋 %d 秒' % (filename, time_to_download))

def main():
    start = time()
    p1 = Process(target=download_task, args=('Python介綍.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


# 当我们在程序中创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间
# 共享数据的时候需要通过其他方法处理，比如Queue,这是一个可以被多个进程共享的队列

