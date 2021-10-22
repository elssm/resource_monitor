import logging
import multiprocessing
import os

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
    logging.basicConfig(level=logging.DEBUG)
    current_process = psutil.Process()
    p = multiprocessing.Process(target=now)
    p.start()

    m = Monitor(p.pid,1,40)
    m.start()
    p.join()
    m.join()
    logging.debug("m is succ")
    print(m.get_monitor_information())