import platform

system_information = {
    "os": platform.system()
}
if __name__ == '__main__':
    print(system_information["os"])