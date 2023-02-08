from flask import render_template, jsonify, redirect, url_for, request
import werkzeug
from system_monitor import app, api, Resource
import json
import subprocess
import os

from system_monitor.system.systemAddress import system_ip
import pandas as pd

with open('system_monitor/config.json') as f:
    data = json.load(f)

# /systemdata
system_path = 'system_data.csv'

# /dockerdata
docker_path = 'docker.csv'


# simple API
class System_Json(Resource):
    def get(self):
        system_data = pd.read_csv(system_path)
        system_data = system_data.to_dict()
        return {'System data': system_data}, 200


class Docker_Json(Resource):
    def get(self):
        docker_data = pd.read_csv(docker_path)
        docker_data = docker_data.to_dict()
        return {'Docker data': docker_data}, 200


api.add_resource(System_Json, '/systemjson')
api.add_resource(Docker_Json, '/dockerjson')

interval = data["SystemMonitor"]["interval_time_sec"]


# Endpoints
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title="Home Page")


@app.route('/system')
def my_system():
    with open("system_data.csv") as file:
        return render_template('system_page.html', data=file, number=interval, title='Machine Monitor Page')


@app.route('/docker')
def my_docker():
    with open("docker.csv") as file:
        return render_template('docker_page.html', data=file, number=interval, title='Docker Monitor Page')


@app.route("/help")
def help_page():
    return render_template('help.html', title='Help Page')


@app.route("/dockerhelp")
def docker_help_page():
    return render_template('docker_help.html', title='Docker Help Page')


@app.route("/config")
def config_page():
    return render_template('config.html', title='Config')


@app.route("/log")
def Log_page():
    logs = []
    ids = []
    with open("docker.csv") as f:
        for line in f:
            ids.append(line.split(",")[1])
    for item in ids:
        with open(f"{item}.html", "r") as f:
            logs.append(f.read())
    return render_template('log.html', logs=logs)



# Reboot the system
@app.route("/reboot", methods=['GET', 'POST'])
def reboot():
    password = "merlin#0"
    subprocess.run(f"echo {password} | sudo -S reboot", shell=True, check=True)
    return "System is rebooting", 200




# Error Handler
@app.errorhandler(werkzeug.exceptions.NotFound)
def Notfound(e):
    return jsonify(error=str(e)), e.code
