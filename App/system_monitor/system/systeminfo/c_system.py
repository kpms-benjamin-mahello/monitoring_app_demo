#!/usr/bin/python3

import json
import platform
import time
from datetime import datetime
import csv
import subprocess
import psutil
import shutil

from system_monitor.system.systemAddress import system_ip
from system_monitor.system.systemAddress.system_ip import check_ip


def system():
    # read config,json file
    with open('system_monitor/config.json') as f:
        data = json.load(f)

        mounting_point = data['SystemMonitor']['disk']

    # Computer name
    computer_name = platform.node()

    # system version
    version = system_ip.my_os

    # system Local time
    now = datetime.now()
    system_local_time = now.strftime("%H:%M:%S")

    # system uptime
    uptime_used = round((time.time() - psutil.boot_time()), 3)

    # Calculate days, hours, minutes, and seconds
    days = int(uptime_used // (24 * 3600))
    uptime_used = uptime_used % (24 * 3600)
    hours = int(uptime_used // 3600)
    uptime_used %= 3600
    minutes = int(uptime_used // 60)
    uptime_used %= 60
    seconds = int(uptime_used)

    # Format uptime in the form DDD HH:MM:SS
    uptime_used_formatted = f"{days:03d} {hours:02d}:{minutes:02d}:{seconds:02d}"

    # get ip address from ipaddr.py
    my_ip = check_ip()

    # cpu load
    my_cpu_load = psutil.cpu_percent(0.5)

    # Ram Usage
    # Get system memory Usage
    ram = psutil.virtual_memory()

    # Unit function to convert Ram size
    def unit(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    used_ram = unit(ram.used)

    # Disk Usage

    result = subprocess.run(["df", "-h"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")

    device_line = [line for line in output.split("\n") if mounting_point in line][0]
    available_space = device_line.split()[3]

    # Write data in csv

    data = [computer_name, system_local_time, uptime_used_formatted, my_ip, my_cpu_load, used_ram, available_space,
            version]

    # header = ['Computer name', ' System Time', 'Uptime', 'IP Address', 'Cpu Load','Ram Usage', 'Disk space', 'Os Version']

    with open('system_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        # write the header
        # writer.writerow(header)

        # write the data
        writer.writerow(data)
