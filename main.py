import logging
import multiprocessing
import os
import time


def now():
    for i in range(50000000):
        time.sleep(1)
        print(i)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    pn = multiprocessing.Process(target=now, name="normal process")
    pn.start()
    print(os.getpid())
    print(pn.pid)