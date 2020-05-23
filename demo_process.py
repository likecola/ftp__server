"""
创建进程process
"""
from time import sleep
import multiprocessing as mp


def fun():
    print("开始执行")
    sleep(2)
    print("执行完了")


p = mp.Process(target=fun)

p.start()
print("原进程开始执行")
sleep(3)
print("原进程执完了")

p.join()
