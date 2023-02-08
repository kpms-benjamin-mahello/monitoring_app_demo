#!/usr/bin/python3

import psutil

def get_used_disk_size():
    disk = psutil.disk_partitions()[0]
    mount_point = input("Enter the mount point: ")
    return disk_usage.used

used_disk_size = get_used_disk_size()
print("Used disk size: ", used_disk_size, "bytes")
