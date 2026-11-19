from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "gta6_db",
}


def conectar_db():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nome = request.form["nome"]
        nick_jogo = request.form["nick_jogo"]
        vai_jogar = request.form["vai_jogar"]

        conn = conectar_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO jogadores (nome, nick_jogo, vai_jogar) VALUES (%s, %s, %s)",
            (nome, nick_jogo, vai_jogar),
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for("dados"))

    return render_template("formulario.html")


@app.route("/dados")
def dados():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, nick_jogo, vai_jogar FROM jogadores ORDER BY id DESC")
    jogadores = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("dados.html", jogadores=jogadores)


if __name__ == "__main__":
    app.run(debug=True)