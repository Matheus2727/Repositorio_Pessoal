from flask import Flask, render_template, request, redirect, session
from werkzeug.security import check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "Ss123$%¨"


def get_db():
    #não existe ainda esse banco
    return sqlite3.connect("DB\DB.db")

def fazer_o_flow():
    print("fiz o flow")
    return "resultado do flow"

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/flamengo")
def flamengo():
    resultado = fazer_o_flow()

    return resultado


if __name__ == "__main__":
    app.run(debug=True)




