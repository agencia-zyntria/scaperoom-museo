from datos import taquilla_28, taquilla_75
from funciones_comunes import decir, preguntar

INTRO = "Entras en el vestuario de empleados. Huele a café y a sudor."


def pedir_codigo(item):
    """Taquillas: 3 intentos para el candado. True si acierta."""
    decir(f"La {item['name']} tiene un candado de números. Tienes 3 intentos.")
    decir(f"Hay una nota pegada: '{item['hint']}'")
    for numero_intento in range(1, 4):
        intento = preguntar(f"Intento {numero_intento} de 3. Escribe el código: ")
        if intento == item["code"]:
            decir("¡Clic! El candado se abre.")
            return True
        decir("Código incorrecto.")
    decir("Has gastado los 3 intentos. Vuelve a intentarlo más tarde.")
    return False


ACCIONES = {
    taquilla_28["name"]: pedir_codigo,
    taquilla_75["name"]: pedir_codigo,
}