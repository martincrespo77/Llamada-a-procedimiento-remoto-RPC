# Verificador de contraseñas – Arquitectura y Uso

Aplicación cliente/servidor para validar contraseñas vía REST/HTTP con JSON. Incluye interfaz web, cliente de consola y lógica de negocio separada.

## Arquitectura
- `main.py` / `server.py`: servidor Flask (API REST + vistas) en `127.0.0.1:8000`.
- `servicio.py`: lógica de validación (reglas de contraseña).
- `templates/interfaz.html`: interfaz web servida por Flask (`/` y `/web_cliente`).
- `web_cliente.html`: cliente web estático (funciona con el servidor en 8000).
- `client.py`: cliente de consola que consume el endpoint REST.
- Dependencias: Flask, requests (ver `requirements.txt` / `pyproject.toml`).
- Ejecución directa en Windows: `start_server.bat` (activa venv si existe, levanta servidor y abre la UI).

## Reglas de validación
- Mínimo 8 caracteres.
- Al menos 1 mayúscula.
- Al menos 1 minúscula.
- Al menos 1 número.
- Al menos 1 caracter especial de: `!@#$%^&*()-+[]{};:'",.<>/?\|`~`

## Instalación
```bash
# Activar venv (PowerShell)
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución
```bash
# Servidor (Flask)
python main.py   # o python server.py
# Escucha en http://127.0.0.1:8000

# Cliente de consola
python client.py
```

Interfaz web:
- Servida por Flask: `http://127.0.0.1:8000/` (alias `/web_cliente`).
- Cliente estático local: abrir `web_cliente.html` (usa 127.0.0.1:8000 por defecto).

## Ejecución rápida en Windows
```bat
start_server.bat
```
Activa el venv si existe, arranca `python main.py` y abre el navegador en `http://127.0.0.1:8000/`.

## API REST
- Método: `POST /api/v1/validarPassword`
- Body JSON:
```json
{ "password": "tu_contrasena" }
```
- Respuesta 200:
```json
{ "valida": true|false, "motivo": "detalle" }
```
- Errores de entrada: 400 con `{ "error": "..." }`

## Notas de seguridad
- Tráfico en texto plano (HTTP). Para producción, usar HTTPS y un WSGI detrás de proxy.
- Servidor ligado a `127.0.0.1` por defecto (no expuesto a la red).
- Manejo básico de errores y validación de entrada; sin autenticación.

## Estructura rápida
```
trabajoRemoto/
├─ main.py
├─ server.py
├─ servicio.py
├─ client.py
├─ templates/
│  └─ interfaz.html
├─ web_cliente.html
├─ requirements.txt
├─ pyproject.toml
└─ start_server.bat
```

## Para compartir/comprimir el proyecto
Incluye solo el código y metadatos necesarios; excluye entornos virtuales y cachés.
- Incluir: `main.py`, `server.py`, `servicio.py`, `client.py`, `templates/interfaz.html`, `web_cliente.html`, `requirements.txt`, `pyproject.toml`, `start_server.bat`, `README.md`, `Trabajo.md` (si quieres adjuntar el informe).
- Excluir: `.venv/`, `__pycache__/`, archivos temporales o binarios.
Si el receptor está en Windows, puede descomprimir y ejecutar `start_server.bat`. En otros sistemas, usar `pip install -r requirements.txt` y `python main.py`.

## Troubleshooting
- Si no ves la interfaz, verifica que el servidor esté corriendo y usa `http://127.0.0.1:8000/` con Ctrl+F5.
- Si cambias el puerto, ajusta `client.py` y las URLs en los HTML (ya intentan reemplazar 5000→8000 automáticamente).
