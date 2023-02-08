#!/usr/bin/python3

import subprocess
import os

def reboot():
    password = 'merlin#0'
    subprocess.run(f"echo {password} | sudo -S reboot", shell=True, check=True)
    # subprocess.call("sudo reboot", shell=True)
    # return render_template('reboot.html')

reboot()
