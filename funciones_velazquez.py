from funciones_comunes import decir

INTRO = "Estás en la sala Velázquez. Las puertas se han cerrado tras de ti."

ACCIONES = {}   # ningún objeto tiene acertijo en esta sala


def visitar_aseo():
    """Sala trampa: el jugador entra, no hay nada y vuelve."""
    decir("")
    decir("Abres la puerta A... es un aseo. Solo hay un lavabo y un espejo.")
    decir("Aquí no hay salida. Vuelves a la sala Velázquez.")