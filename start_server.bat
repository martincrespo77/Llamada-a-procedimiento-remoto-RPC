@echo off
REM Lanza el servidor Flask y abre la interfaz web.
REM Uso: doble clic o ejecutar en consola dentro del proyecto.

cd /d "%~dp0"

REM Activa el venv si existe
set VENV_ACTIVATE=%~dp0.venv\Scripts\activate.bat
if exist "%VENV_ACTIVATE%" (
    call "%VENV_ACTIVATE%"
)

REM Arranca el servidor en una nueva ventana de consola
start "" cmd /c "python main.py"

REM Pequeña espera y abre el navegador en la UI
ping -n 3 127.0.0.1 >nul
start "" http://127.0.0.1:8000/
