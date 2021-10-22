import logging
from multiprocessing import Process
import os
import psutil


class Monitor(Process):
    def __init__(self, pid, interval, threshold,q):
        """
        监控一个进程的监控器
        :param pid: 监控进程的 pid
        :param interval: 每次监控的时间间隔
        :param threshold:
        """
        super().__init__()
        self.monitor_pid = pid
        self.monitor_processes = psutil.Process(pid)
        self.detect_information = None
        self.interval = interval
        self.threshold = threshold
        self.q = q

    def run(self):
        point_information = {"mem": [], "cpu": []}
        logging.debug(f"{self.monitor_processes}")
        try:
            while self.monitor_processes.is_running():
                logging.debug(point_information)
                mem_percent = self.monitor_processes.memory_percent()
                cpu_percent = self.monitor_processes.cpu_percent(interval=self.interval)
                if mem_percent == 0 and cpu_percent == 0:
                    continue
                point_information["mem"].append(mem_percent)
                point_information["cpu"].append(cpu_percent)
                print("point_information",point_information)
        except:
            logging.info("monitor success")
        finally:
            logging.debug(f"detect information is {point_information}")
        self.detect_information = point_information
        self.q.put(self.detect_information)
        return self.q
        # print("detect_information",self.detect_information )

    def get_monitor_information(self):
        # print("get information is ",self.detect_information)
        logging.debug(f"get information is {self.detect_information}")
        return self.detect_information