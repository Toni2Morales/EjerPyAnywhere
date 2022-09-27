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
    print("aaaaaaaa")


