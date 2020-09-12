from flask import Flask
from .config import DevConfig

#initializing application
app = Flask(__name__)
from app import views

# Setting up configuration
app.config.from_object(DevConfig)

