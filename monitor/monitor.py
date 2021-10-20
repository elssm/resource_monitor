import os

import psutil


class Monitor:
    def __init__(self, pids) -> None:
        self.pids = pids
        self.psutil_process = self.parse_monitor_process()

    def parse_monitor_process(self):
        if type(self.pids) is int:
            psutil_process = [psutil.Process(self.pids)]
        else:
            psutil_process = []
            for pid in self.pids:
                psutil_process.append(psutil.Process(pid))
        return psutil_process


class WindowsMonitor(Monitor):

    def __init__(self, pids) -> None:
        super().__init__(pids)

    def get_cpu_information(self):
        pass


class LinuxMonitor(Monitor):

    def __init__(self, pids) -> None:
        super().__init__(pids)


if __name__ == '__main__':
    pid = os.getpid()
    m = WindowsMonitor(pid)
    print(m.psutil_process)