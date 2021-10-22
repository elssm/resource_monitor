import logging
import multiprocessing
from multiprocessing import set_start_method,Queue
import os,time

import psutil

from monitor.monitor import Monitor


def mul(a, b):
    logging.debug(f"a is {a},b is {b}")
    return a ** b


def now():
    for i in range(1):
        mul(i+100,1<<22)
    logging.debug("process out")


if __name__ == '__main__':
    set_start_method('fork')
    Q = Queue(10)
    logging.basicConfig(level=logging.DEBUG)
    current_process = psutil.Process()
    p = multiprocessing.Process(target=now)
    p.start()

    m = Monitor(p.pid,1,40,Q)
    m.start()
    m.join()
    p.join()
    print("main get",Q.get())
    logging.debug("m is succ")