#!/usr/bin/python3

import psutil

def get_disk_usage():
    mount_point = input("Enter the mount point: ")
    disk_usage = psutil.disk_usage(mount_point)
    return disk_usage.used

used_disk_size = get_disk_usage()
print("Used disk size: ", used_disk_size, "bytes")
