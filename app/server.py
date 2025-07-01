from flask import Flask, render_template, request, jsonify
from data import VuelosData
import os

app = Flask(__name__, template_folder="../templates")  # usa '../templates' si estás en app/
datos = VuelosData()

@app.route("/")
def home():
    return render_template("consultar.html")

@app.route("/consultar")
def consultar():
    vuelos = datos.leer_vuelos()
    return jsonify(vuelos)

@app.route("/reservar", methods=["POST"])
def reservar():
    vuelo = request.form["vuelo"]
    asiento = request.form["asiento"]
    nombre = request.form["nombre"]

    if datos.reservar(vuelo, asiento, nombre):
        return "Reserva exitosa"
    else:
        return "Asiento ya reservado", 400

@app.route("/disponibilidad")
def disponibilidad():
    vuelos = datos.leer_vuelos()
    return render_template("disponibilidad.html", vuelos=vuelos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
