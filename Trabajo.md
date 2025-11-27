## 1. “Implementar un cliente–servidor usando RPC o REST…”

👉 **Cumplido**

* Usamos **REST sobre HTTP** con JSON:

  * Servidor: `Flask` con endpoint `POST /api/v1/validarPassword` (`rutas.py`).
  * Cliente: `client.py` que hace la llamada remota y recibe el resultado.
* La función remota es clara:
  `validar_password(password: str) -> (bool, str)` en `servicio.py`.
  Eso es exactamente una **llamada a procedimiento remoto**, solo que implementada con REST.

La consigna dice explícitamente que puede ser **REST**, así que por ese lado estás cubierta.

---

## 2. “Buenas prácticas de programación y aspectos de seguridad (código seguro)”

👉 **Conceptualmente cumplido**, y se puede justificar:

* Lógica de negocio separada en `servicio.py` (**modelo**).
* Rutas / API HTTP separadas en `rutas.py` (**controlador/vista**).
* Punto de entrada limpio en `main.py`.
* Cliente encapsulado en clase `ClienteVerificadorPassword` con manejo de errores.
* Seguridad en código:

  * Validás entrada (`password` no nulo/vacío, tipo string).
  * No usás `debug=True` en Flask.
  * El servidor escucha en `127.0.0.1` (no expuesto a toda la red por defecto).
  * Manejo de excepciones con respuesta 400 / 500 controlada (no stacktrace al usuario).
  * Reglas de validación centralizadas (fácil de mantener y extender).

**Lo que tenés que hacer en el informe**:
explicar estas cosas como “buenas prácticas” y marcar al menos una **mejora** respecto a una versión más ingenua (por ejemplo: antes sin manejo de errores ni validación de JSON; después, con esto agregado).

---

## 3. “Comprobar funcionamiento en la red, capturar y analizar tramas TCP (y UDP si aplica)…”

👉 **Técnicamente cumplido si vos hacés las pruebas**:

* Tu sistema usa **HTTP sobre TCP**, así que:

  * Vas a ver paquetes **TCP** con destino al puerto `5000`.
  * No hay UDP, y la consigna dice “UDP si aplicara”: en tu caso, no aplica.
* Podés:

  * Levantar servidor (`python main.py`).
  * Ejecutar cliente (`python client.py`) y/o interfaz web.
  * Capturar con **Wireshark** la interfaz correspondiente (`lo` o adaptador de red).
  * Filtrar por `tcp.port == 5000` o `http`.

**En el informe**:
tenés que incluir capturas + descripción de:

* Quién es cliente, quién es servidor.
* Qué protocolo en cada capa (HTTP / TCP / IP / enlace).
* Qué puerto usa el servidor.

---

## 4. “Relevamiento de conexiones, puertos y protocolos – modelo DARPA/Internet”

👉 **Cumplido si escribís el análisis**, el código ya genera todo lo que necesitás:

* Podés usar `netstat`, `ss`, `lsof`:

  * Ver que `python` escucha en `127.0.0.1:5000` (servidor).
  * Ver las conexiones creadas por el cliente.
* En el informe, para el punto **c) y d)**:

  * Puertos: 5000/TCP (servidor), puerto efímero TCP en el cliente.
  * Protocolos:

    * Capa aplicación: HTTP + JSON.
    * Transporte: TCP.
    * Internet: IP.
    * Acceso a red: Ethernet / Wi-Fi según el entorno.

La aplicación está bien pensada para explicar el modelo DARPA sin complicarse.

---

## 5. “Analizar seguridad desde código, red y sistema operativo + proponer/mejorar”

👉 **Totalmente compatible con lo que hicimos**, falta escribirlo claro:

* **Desde el código fuente**:

  * Lo que ya comentamos (validación, manejo de errores, sin debug, etc.).
  * Vulnerabilidades evidentes: tráfico en texto plano, no hay autenticación, etc.
* **Desde la red**:

  * HTTP sin cifrar → susceptible a sniffing / MITM.
  * Exposición del puerto 5000 si lo abrís a toda la red.
* **Desde el sistema operativo**:

  * Podés correr el servidor con un usuario sin privilegios.
  * Ajustar permisos de archivos (`chmod`).
  * Evaluar qué pasa si otro usuario intenta ejecutar/modificar los scripts.

**“Proponer e implementar una mejora”**
La mejora la podés plantear como:

* Mejora **de código**:
  pasar de una versión sin manejo de JSON/errores a la versión actual con:

  * chequeo `request.is_json`,
  * respuestas 400 bien formadas,
  * función `validar_password` centralizada.
* Mejora **de despliegue** (aunque sea teórica):

  * Proponer configurar HTTPS con un reverse proxy (Nginx) en entorno real.
  * Limitar el binding de Flask a `127.0.0.1` (ya está) y documentarlo como decisión de seguridad.

En el informe, contás la “versión inicial” y la “versión mejorada” aunque tu código ya esté en la versión buena.

---

## 6. “Asignar permisos adecuados y analizar qué sucede con distintos usuarios”

👉 **Esto no depende del código**, sino de cómo lo corrés:

* En Linux, por ejemplo:

  * Guardás los archivos en `/home/tu_usuario/practica_rpc/`.
  * Ajustás permisos:

    * `chmod 700 main.py client.py` → solo tu usuario puede ejecutar.
    * Mostrás qué pasa si otro usuario intenta ejecutar.
  * También podés comentar que el servidor se ejecuta con un usuario sin privilegios (no `root`).

Esto se describe en el informe dentro del punto **e) vulnerabilidades OS** y **f) mitigaciones**.

---

## 7. “Productos a evaluar:”

1. **Cliente–servidor funcionando en la red**
   ✅ Lo tenés: servidor Flask + cliente consola + cliente web.

2. **Informe con puntos a)–f)**

   * a) Aplicación cliente–servidor → ya tenemos la Sección 3 escrita.
   * b) Escenario de red → lo podemos redactar fácil con tu topología.
   * c) Conexiones abiertas → salidas de `netstat/ss` + explicación.
   * d) Protocolos y servicios → HTTP/TCP/IP + Wireshark.
   * e) Vulnerabilidades (código, red, SO) → ya las venimos marcando.
   * f) Mitigación → decisiones que ya tomamos + mejoras propuestas.

---
