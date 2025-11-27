import json
import requests


class ClienteVerificadorPassword:
    def __init__(self, servidor_url="http://127.0.0.1:8000/api/v1/validarPassword"):
        self.servidor_url = servidor_url
        self.encabezados = {
            "Content-Type": "application/json",
            "User-Agent": "ClienteVerificadorPassword/1.0",
        }

    def validar_password_remota(self, password: str):
        """Envio de la contrasena al servidor con manejo de errores HTTP/red."""
        try:
            datos = {"password": password}
            resp = requests.post(
                self.servidor_url,
                headers=self.encabezados,
                data=json.dumps(datos),
                timeout=10,
            )
        except requests.exceptions.ConnectionError:
            return {"error": "No se pudo conectar con el servidor. Verifique que esta en ejecucion."}
        except requests.exceptions.Timeout:
            return {"error": "Timeout: el servidor tardo demasiado en responder."}
        except requests.exceptions.RequestException as exc:
            return {"error": f"Error de conexion: {exc}"}

        if resp.status_code == 200:
            try:
                return resp.json()
            except ValueError:
                return {"error": "Respuesta del servidor no es JSON valida."}

        try:
            return resp.json()
        except ValueError:
            return {"error": f"Error HTTP {resp.status_code}", "detalles": resp.text}

    def mostrar_resultado(self, resultado: dict):
        """Imprime un resultado amigable en consola."""
        if resultado is None:
            return

        if "error" in resultado:
            print(f"Error: {resultado.get('error')}")
            if "detalles" in resultado:
                print(f"Detalles: {resultado.get('detalles')}")
            return

        valida = resultado.get("valida", False)
        motivo = resultado.get("motivo", "Sin motivo especificado")
        estado = "CONTRASENA VALIDA" if valida else "CONTRASENA NO VALIDA"
        print(estado)
        print(f"Motivo: {motivo}")

    def ejecutar(self):
        """Bucle interactivo con el usuario."""
        print("=" * 50)
        print("    VERIFICADOR DE CONTRASENAS - CLIENTE")
        print("=" * 50)
        print("Valida contrasenas contra un servidor remoto.\n")

        while True:
            password = input("Ingrese una contrasena a validar (o 'salir' para terminar): ").strip()
            if password.lower() == "salir":
                print("Hasta luego.")
                break
            if not password:
                print("Por favor ingrese una contrasena.\n")
                continue

            print("Validando en el servidor...")
            resultado = self.validar_password_remota(password)
            self.mostrar_resultado(resultado)
            print()

            continuar = input("Desea validar otra contrasena? (s/n): ").strip().lower()
            if continuar not in ["s", "si", "y", "yes"]:
                print("Hasta luego.")
                break
            print()


def main():
    cliente = ClienteVerificadorPassword()
    cliente.ejecutar()


if __name__ == "__main__":
    main()
