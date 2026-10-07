import os
import unicodedata
from datos import object_relations, INIT_GAME_STATE

SEPARADOR = "=" * 50


# ---------- Entrada / salida (la interfaz puede sustituirlas) ----------
def _limpiar_terminal():
    os.system("cls" if os.name == "nt" else "clear")   # cls en Windows


_salida = print
_entrada = input
_limpiar = _limpiar_terminal

# ---------- Configuración de la interfaz ----------
def configurar_io(salida, entrada, limpiar):
    """Cambia cómo el juego muestra texto, pide respuestas y limpia la pantalla."""
    global _salida, _entrada, _limpiar
    _salida = salida
    _entrada = entrada
    _limpiar = limpiar

# ---------- Funciones para mostrar texto y pedir respuestas ----------
def decir(texto=""):
    _salida(texto)


def preguntar(texto):
    return _entrada(texto).strip()


def limpiar():
    _limpiar()


# ---------- Estado de la partida ----------
def crear_game_state():
    """Devuelve una copia nueva de INIT_GAME_STATE para empezar una partida."""
    return {
        "current_room": INIT_GAME_STATE["current_room"],
        "keys_collected": list(INIT_GAME_STATE["keys_collected"]),
        "target_room": INIT_GAME_STATE["target_room"],
    }


# ---------- Búsqueda ----------
def normalizar(texto):
    """Minúsculas y sin tildes, para que 'venus del delfin' también valga."""
    texto = unicodedata.normalize("NFD", texto.strip().lower())
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")

# ---------- Búsqueda de ítems ----------
def buscar_en_sala(nombre_item, sala):
    """Busca un ítem de la sala por nombre o por su número en la lista."""
    items = object_relations[sala["name"]]
    if nombre_item.isdigit():
        posicion = int(nombre_item) - 1
        if 0 <= posicion < len(items):
            return items[posicion]
        return None
    for item in items:
        if normalizar(item["name"]) == normalizar(nombre_item):
            return item
    return None


# ---------- Puertas ----------
def puede_abrir(puerta, game_state):
    """True si alguna llave del jugador tiene esa puerta como target."""
    for llave in game_state["keys_collected"]:
        if llave["target"] == puerta:
            return True
    return False


def cruzar_puerta(puerta, game_state):
    """Devuelve la sala del otro lado, o None si la puerta está cerrada."""
    if not puede_abrir(puerta, game_state):
        decir(f"La {puerta['name']} está cerrada. Necesitas su llave.")
        return None
    sala_a, sala_b = object_relations[puerta["name"]]
    if game_state["current_room"] == sala_a:
        return sala_b
    return sala_a


# ---------- Objetos ----------
def coger_contenido(item, game_state):
    """Guarda las llaves y lee las pistas que haya dentro de un ítem."""
    contenido = object_relations.get(item["name"], [])
    if not contenido:
        decir(f"Examinas {item['name']}. No hay nada interesante.")
        return
    for objeto in contenido:
        if objeto["type"] == "key":
            if objeto in game_state["keys_collected"]:
                decir(f"Aquí estaba la {objeto['name']}, pero ya la tienes.")
            else:
                game_state["keys_collected"].append(objeto)
                decir(f"¡Encuentras la {objeto['name']}!")
        elif objeto["type"] == "clue":
            decir(f"Pista: {objeto['text']}")


# ---------- Inventario ----------
def mostrar_inventario(game_state):
    """Enseña las llaves que lleva el jugador."""
    nombres = [llave["name"] for llave in game_state["keys_collected"]]
    if nombres:
        decir("  Inventario: " + ", ".join(nombres))
    else:
        decir("  Inventario: vacío")


# ---------- Bucle de una sala (el mismo para todas) ----------
def mostrar_sala(sala, game_state):
    decir("")
    decir(SEPARADOR)
    decir(f"  {sala['name'].upper()}")
    decir(SEPARADOR)
    for numero, item in enumerate(object_relations[sala["name"]], start=1):
        decir(f"  {numero}. {item['name']}")
    decir("-" * 50)
    mostrar_inventario(game_state)
    decir("")


def jugar_sala(game_state, acciones):
    """El jugador examina cosas hasta que cruza una puerta.
    'acciones' es un diccionario {nombre del ítem: función} con los acertijos
    de la sala. La función devuelve True si el jugador lo supera.
    Devuelve la sala a la que pasa el jugador."""
    sala = game_state["current_room"]
    while True:
        mostrar_sala(sala, game_state)
        eleccion = preguntar("¿Qué quieres examinar? (nombre o número) > ")
        limpiar()   # borra la pantalla antes de mostrar el resultado

        item = buscar_en_sala(eleccion, sala)

        if item is None:
            decir("Aquí no hay nada con ese nombre.")
            continue

        if item["type"] == "door":
            destino = cruzar_puerta(item, game_state)
            if destino is not None:
                return destino
            continue

        accion = acciones.get(item["name"])
        if accion is None or accion(item):
            coger_contenido(item, game_state)