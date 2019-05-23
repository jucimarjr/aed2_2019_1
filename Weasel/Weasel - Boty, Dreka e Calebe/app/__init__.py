from flask import Flask
from app import *
from flask_wtf import *
from flask_script import Manager

app = Flask(__name__)
app.config.from_object('config')

manager = Manager(app)

from app.models import forms
from app.controllers import default
