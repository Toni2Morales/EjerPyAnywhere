from flask import Flask, request
import sqlite3

app = Flask(__name__)
app.config["Debug"] = True

@app.route("/", methods = ["GET"])
def entrada():
    return("¡Bienvenido a la página web de Antonio!")
    


