from flask import Flask
from data import get_data


sicei = Flask(__name__)

@sicei.route("/")
def index():
    return 'Welcome to sicei application'

@sicei.route("/alumnos")
def get_alumnos():
    data = get_data()
    return {"alumnos": data}


if __name__ == "__main__":
    sicei.run()
