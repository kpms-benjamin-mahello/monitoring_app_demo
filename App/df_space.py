#!/usr/bin/python3

import os

def get_available_space(path):
    statvfs = os.statvfs(path)
    available = statvfs.f_frsize * statvfs.f_bavail
    return available

print("Available disk space (bytes):", get_available_space("/dev/sda"))
