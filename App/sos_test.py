#:wq

total = int()
used  = int()
free  = int()

for disk in psutil.disk_partitions():
    if disk.fstype:
        total += int(psutil.disk_usage(disk.mountpoint).total)
        used  += int(psutil.disk_usage(disk.mountpoint).used)
        free  += int(psutil.disk_usage(disk.mountpoint).free)

print(f'''    
    TOTAL DISK SPACE : {round(total / (1024.0 ** 3), 4)} GiB
    USED DISK SPACE  : {round(used / (1024.0 ** 3), 4)} GiB
    FREE DISK SPACE  : {round(free / (1024.0 ** 3), 4)} GiB
''')
