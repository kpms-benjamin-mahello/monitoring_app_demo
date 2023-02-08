import subprocess
import json
import platform

# detect operating system
my_os = platform.system()

# read config,json file
with open('system_monitor/config.json') as f:
    data = json.load(f)

intf = data['SystemMonitor']['ethernetPort']


def check_ip():
    try:
        intf_ip = subprocess.getoutput("ip address show dev " + intf).split()
        intf_ip = intf_ip[intf_ip.index('inet') + 1].split('/')[0]
        return intf_ip
    except ValueError as ve:
        return f'Not support in {my_os}'


