import requests
from flask import Flask

project = Flask(__name__)

@project.route('/')
def home():
    return "<p>Okay Microsoft</p>"

project.run(debug=True)
