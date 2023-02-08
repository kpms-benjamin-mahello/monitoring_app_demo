from flask import Flask
from flask_apscheduler import APScheduler
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
app.config.from_object("config.DevelopmentConfig")

scheduler = APScheduler()

from system_monitor.routes import route


