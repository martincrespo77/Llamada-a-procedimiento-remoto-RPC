from server import app


def main():
    print("=" * 50)
    print("Servidor RPC/REST - Verificador de Contrasenas")
    print("Escuchando en http://127.0.0.1:8000")
    print("=" * 50)
    app.run(host="127.0.0.1", port=8000, debug=False)


if __name__ == "__main__":
    main()
