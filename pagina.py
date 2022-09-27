from flask import Flask, request
import sqlite3
import pickle

app = Flask(__name__)
app.config["Debug"] = True

@app.route("/", methods = ["GET"])
def entrada():
    return("¡Bienvenido a la página web de Antonio!")

@app.route("/prediccion", methods=['GET'])
def prediction():
    tv = request.args.get("tv", None)
    radio = request.args.get("radio", None)
    newspaper = request.args.get("newspaper", None)
    with open("advertising_model", "rb") as f:
        modelo = pickle.load(f)
    prediccion = modelo.predict([[tv, radio, newspaper]])
    return str(prediccion)


