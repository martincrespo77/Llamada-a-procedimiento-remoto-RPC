from flask import Flask, request, jsonify, render_template, redirect, url_for
from servicio import validar_password

app = Flask(__name__)


@app.post("/api/v1/validarPassword")
def validar_password_endpoint():
    """
    Endpoint REST: espera JSON {"password": "..."} y devuelve {"valida": bool, "motivo": str}.
    """
    if not request.is_json:
        return jsonify({"error": "El contenido debe ser application/json"}), 400

    data = request.get_json(silent=True) or {}
    if "password" not in data:
        return jsonify({"error": "El cuerpo de la solicitud debe incluir el campo 'password'."}), 400

    password = data.get("password", "")
    valida, motivo = validar_password(password)
    return jsonify({"valida": valida, "motivo": motivo}), 200


@app.get("/")
def index():
    """Vista principal usando template."""
    return render_template("interfaz.html")


@app.get("/web_cliente")
def web_cliente():
    """Alias a la misma interfaz."""
    return redirect(url_for("index"))


if __name__ == "__main__":
    print("=" * 50)
    print("Servidor RPC/REST - Verificador de Contrasenas")
    print("Escuchando en http://127.0.0.1:8000")
    print("=" * 50)
    app.run(host="127.0.0.1", port=8000, debug=False)
