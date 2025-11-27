import re

# Set de caracteres especiales permitidos
SPECIALS = "!@#$%^&*()-+[]{};:'\",.<>/?\\|`~"
SPECIALS_PATTERN = "[" + re.escape(SPECIALS) + "]"


def validar_password(password: str):
    """
    Valida una contrasena segun reglas basicas de seguridad.
    Devuelve solo el primer error encontrado.
    """
    if password is None or password == "":
        return False, "La contrasena no puede estar vacia."

    if len(password) < 8:
        return False, "La contrasena debe tener al menos 8 caracteres."

    if not re.search(r"[A-Z]", password):
        return False, "La contrasena debe contener al menos una letra mayuscula."

    if not re.search(r"[a-z]", password):
        return False, "La contrasena debe contener al menos una letra minuscula."

    if not re.search(r"\d", password):
        return False, "La contrasena debe contener al menos un numero."

    if not re.search(SPECIALS_PATTERN, password):
        return False, "La contrasena debe contener al menos un caracter especial (!@#$%^&*()-+[]=\\{};:'\",.<>/?|`~)."

    return True, "La contrasena cumple con los requisitos minimos."
