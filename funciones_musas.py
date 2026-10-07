from datos import carlos, vigilante
from funciones_comunes import decir, preguntar

INTRO = "Entras en la Sala de las Musas. Varias esculturas te observan."


def adivinar_numero(item):
    """Carlos V: adivinar un número del 1 al 5. True si acierta."""
    decir(f"La estatua de {item['name']} esconde un número del 1 al 5.")
    intentos = item["attempts"]
    while intentos > 0:
        respuesta = preguntar(f"Adivina el número ({intentos} intentos): ")
        try:
            numero = int(respuesta)
        except ValueError:
            decir("Eso no es un número. Inténtalo otra vez.")
            continue
        if numero < 1 or numero > 5:
            decir("El número tiene que estar entre 1 y 5.")
            continue
        if numero == item["secret_number"]:
            decir("¡Correcto!")
            return True
        intentos -= 1
        decir("Número incorrecto.")
    decir("Te has quedado sin intentos. Examínalo de nuevo para volver a probar.")
    return False


def par_o_impar(item):
    """Vigilante: par o impar. True si acierta."""
    decir("El vigilante cierra el puño con unas monedas dentro:")
    decir("'Te doy una pista si aciertas esto.'")
    opciones = (item["correct_answer"], item["wrong_answer"])
    while True:
        respuesta = preguntar("¿Tengo un número par o impar de monedas? ").lower()
        if respuesta in opciones:
            break
        decir("Escribe 'par' o 'impar'.")
    if respuesta == item["correct_answer"]:
        decir("¡Correcto!")
        return True
    decir("Incorrecto. Habla otra vez con el vigilante para volver a intentarlo.")
    return False


ACCIONES = {
    carlos["name"]: adivinar_numero,
    vigilante["name"]: par_o_impar,
}