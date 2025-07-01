from flask import Flask, render_template, request, jsonify, redirect, url_for
from data import VuelosData
import os

app = Flask(__name__, template_folder="../templates")  # Ajusta ruta si server.py está en /app
datos = VuelosData()

# Página para el usuario (reservar asiento)
@app.route("/consultar")
def consultar():
    vuelos = datos.leer_vuelos()
    return jsonify(vuelos)


@app.route("/usuario")
def usuario():
    vuelos = datos.leer_vuelos()
    return render_template("usuario.html", vuelos=vuelos)

# Panel del administrador
@app.route("/admin")
def admin():
    vuelos = datos.leer_vuelos()
    return render_template("admin.html", vuelos=vuelos)

# Eliminar una reserva
@app.route("/eliminar", methods=["POST"])
def eliminar():
    vuelo = request.form.get("vuelo")
    asiento = request.form.get("asiento")
    if vuelo and asiento and datos.cancelar(vuelo, asiento):
        return jsonify({"status": "ok", "mensaje": "Reserva eliminada"})
    return jsonify({"status": "error", "mensaje": "Reserva no encontrada"}), 400

# Reiniciar todos los asientos
@app.route("/reiniciar", methods=["POST"])
def reiniciar():
    datos.reiniciar_asientos()
    return jsonify({"status": "ok", "mensaje": "Asientos reiniciados"})

# Página principal que redirige al usuario
@app.route("/")
def home():
    return render_template("index.html")

def leer_vuelos(self):
    self.lectura.acquire()
    vuelos_copia = {
        vuelo: {
            "asientos": self.vuelos[vuelo]["asientos"].copy()
        }
        for vuelo in self.vuelos
    }
    self.lectura.release()
    return vuelos_copia


# Puerto dinámico (para Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



