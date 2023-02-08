#!/bin/sh

import psutil

# Get disk usage information for the specified mounting point
disk = psutil.disk_usage('/')


# Calculate the total disk space (in bytes)
total = disk.total

# Calculate the used disk space (in bytes)
used = disk.used

# Calculate the free disk space (in bytes)
free = disk.free

# Print the results
print(f"Total disk space: {total} bytes")
print(f"Used disk space: {used} bytes")
print(f"Free disk space: {free} bytes"
