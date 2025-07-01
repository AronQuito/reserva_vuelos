from flask import redirect, url_for

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


