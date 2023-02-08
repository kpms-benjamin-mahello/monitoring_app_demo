#!/usr/bin/python3

import threading
from system_monitor import scheduler, app
from system_monitor.docker.docker import running_containers
from system_monitor.system.systeminfo.c_system import system
from system_monitor.routes.route import interval
from system_monitor.mqtt_pub.mqtt_pubs import start_publisher
from system_monitor.mqtt_pub.mqtt_sub import start_subscriber

if __name__ == '__main__':
    pub_thread = threading.Thread(target=start_publisher)
    sub_thread = threading.Thread(target=start_subscriber)
    pub_thread.start()
    sub_thread.start()

    scheduler.add_job(id='Scheduled Task1', func=system, trigger="interval", seconds=interval)
    scheduler.add_job(id='Scheduled Task2', func=running_containers, trigger="interval", seconds=interval)
    scheduler.start()
    app.run(use_reloader=True, host='0.0.0.0', port=5002, debug=True)

