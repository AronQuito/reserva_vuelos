from flask import Flask, render_template, request, jsonify, redirect, url_for
from data import VuelosData
import os

app = Flask(__name__, template_folder="../templates")
datos = VuelosData()

@app.route("/consultar")
def consultar():
    vuelos = datos.leer_vuelos()
    return jsonify(vuelos)

@app.route("/usuario")
def usuario():
    vuelos = datos.leer_vuelos()
    return render_template("usuario.html", vuelos=vuelos)

@app.route("/admin")
def admin():
    vuelos = datos.leer_vuelos()
    return render_template("admin.html", vuelos=vuelos)

@app.route("/eliminar", methods=["POST"])
def eliminar():
    vuelo = request.form.get("vuelo")
    asiento = request.form.get("asiento")
    if vuelo and asiento and datos.cancelar(vuelo, asiento):
        return jsonify({"status": "ok", "mensaje": "Reserva eliminada"})
    return jsonify({"status": "error", "mensaje": "Reserva no encontrada"}), 400

@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    datos.reiniciar_asientos()
    return jsonify({"status": "ok", "mensaje": "Asientos reiniciados"})

@app.route("/reservar", methods=["POST"])
def reservar():
    vuelo = request.form.get("vuelo")
    asiento = request.form.get("asiento")
    nombre = request.form.get("nombre")
    if not asiento or not nombre:
        return "Faltan datos", 400
    if datos.reservar(vuelo, asiento, nombre):
        return redirect(url_for("home"))
    else:
        return "Asiento ya reservado", 400

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



