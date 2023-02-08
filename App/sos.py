#!/usr/bin/python

import psutil


def get_disk_size():
    disk = psutil.disk_partitions()[3]
    disk_usage = psutil.disk_usage(disk.mountpoint)
    return disk_usage.total

disk_size = get_disk_size()
print("Disk size: ", disk_size, "bytes")


