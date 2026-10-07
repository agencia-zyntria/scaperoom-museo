from datos import mesa
from funciones_comunes import decir, preguntar

INTRO = "Entras en la cafetería del Museo del Prado."

# Leer hoja de papel sobre la mesa 4
def leer_hoja(item):
    """Mesa 4: hay una hoja de papel. True si el jugador decide leerla."""
    decir(f"Has encontrado una hoja de papel sobre la {item['name']}.")
    while True:
        respuesta = preguntar("¿Quieres leer la hoja? (si/no): ").lower()
        if respuesta == "si":
            decir("Lees la hoja...")
            return True
        if respuesta == "no":
            decir("Decides no leer la hoja.")
            return False
        decir("Respuesta no válida. Escribe 'si' o 'no'.")


ACCIONES = {
    mesa["name"]: leer_hoja,
}