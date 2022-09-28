from flask import Flask, request
import sqlite3
import pickle
import numpy as np

app = Flask(__name__)
app.config["Debug"] = True

@app.route("/", methods = ["GET"])
def entrada():
    return("¡Bienvenido a la página web de Antonio!")

@app.route("/predict", methods=['GET'])
def prediction():
    tv = request.args.get("tv", None)
    radio = request.args.get("radio", None)
    newspaper = request.args.get("newspaper", None)
    with open("advertising_model", "rb") as f:
        modelo = pickle.load(f)
    prediccion = modelo.predict([[tv, radio, newspaper]])
    return str(prediccion)

@app.route("/ingest_data", methods=['GET'])
def agregar():
    tv = request.args.get("tv", None)
    radio = request.args.get("radio", None)
    newspaper = request.args.get("newspaper", None)
    sales = request.args.get("sales", None)
    connection = sqlite3.connect("Advertising.db")
    cursor = connection.cursor()
    cursor.execute(str("INSERT INTO Advertising(tv, radio, newspaper, sales) VALUES(" + tv + "," + radio + "," + newspaper + "," + sales + ")"))
    num = str(len(cursor.execute("select * from advertising").fetchall()))
    connection.commit()
    connection.close()
    return str("el número de registros de la base de datos ahora es: " + num)

@app.route("/retrain", methods=['GET'])
def reentrenar():
    connection = sqlite3.connect("Advertising.db")
    cursor = connection.cursor()
    with open("advertising_model", "rb") as f:
        modelo = pickle.load(f)
    x = np.array(cursor.execute("select * from advertising").fetchall())[:, :-1]
    y = np.array(cursor.execute("select * from advertising").fetchall())[:, 3]
    modelo.fit(x,y)
    connection.close()
    return "El modelo ha sido reentrenado con los valores añadidos"
