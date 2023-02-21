from flask import Flask

sicei = Flask(__name__)

alumnos = [
    {"nombre": "Desiree Correa", "matricula": "16004107"},
    {"nombre": "Jane Doe", "matricula": "140053173"},
    {"nombre": "John Doe", "matricula": "170004317"},
    {"nombre": "Jan Jansen", "matricula": "17000907"},
    {"nombre": "Erika Mustermann", "matricula": "192004317"},
]

@sicei.get("/alumnos")
def get_alumnos():
    return {"alumnos": alumnos}