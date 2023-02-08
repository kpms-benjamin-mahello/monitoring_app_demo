#!/usr/bin/python3

import subprocess

result = subprocess.run(["df", "-h"], stdout=subprocess.PIPE)
output = result.stdout.decode("utf-8")

mounting_point = "/dev/sda5" # here comes the Mounting point value

device_line = [line for line in output.split("\n") if mounting_point in line][0]
available_space = device_line.split()[3]

print(available_space)

