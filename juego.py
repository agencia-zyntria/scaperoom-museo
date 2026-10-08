import os
import webbrowser
from datos import sala_velazquez, aseo, sala_musas, cafeteria, vestuario
from funciones_comunes import decir, preguntar, crear_game_state, jugar_sala
import funciones_velazquez
import funciones_aseo
import funciones_musas
import funciones_cafeteria
import funciones_vestuario

LETRERO = r"""
 __    __     __  __     ______     ______     ______
/\ "-./  \   /\ \/\ \   /\  ___\   /\  ___\   /\  __ \
\ \ \-./\ \  \ \ \_\ \  \ \___  \  \ \  __\   \ \ \/\ \
 \ \_\ \ \_\  \ \_____\  \/\_____\  \ \_____\  \ \_____\
  \/_/  \/_/   \/_____/   \/_____/   \/_____/   \/_____/

 _____     ______     __            ______   ______     ______     _____     ______
/\  __-.  /\  ___\   /\ \          /\  == \ /\  == \   /\  __ \   /\  __-.  /\  __ \
\ \ \/\ \ \ \  __\   \ \ \____     \ \  _-/ \ \  __<   \ \  __ \  \ \ \/\ \ \ \ \/\ \
 \ \____-  \ \_____\  \ \_____\     \ \_\    \ \_\ \_\  \ \_\ \_\  \ \____-  \ \_____\
  \/____/   \/_____/   \/_____/      \/_/     \/_/ /_/   \/_/\/_/   \/____/   \/_____/

  (Scape room CLI)
  
  """ 
# Qué archivo de funciones corresponde a cada sala
MODULOS = {
    sala_velazquez["name"]: funciones_velazquez,
    aseo["name"]: funciones_aseo,
    sala_musas["name"]: funciones_musas,
    cafeteria["name"]: funciones_cafeteria,
    vestuario["name"]: funciones_vestuario,
}

# Imagen del plano del museo (está en la misma carpeta que este archivo)
MAPA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mapa_museo.png")


def mostrar_mapa():
    """Abre la imagen del plano del museo con el visor de imágenes del sistema."""
    if not os.path.exists(MAPA):
        decir("(No se encuentra la imagen del mapa: mapa_museo.png)")
        return
    try:
        if os.name == "nt":
            os.startfile(MAPA)   # Windows: abre el visor de fotos
        else:
            webbrowser.open("file://" + MAPA)
        decir("Se ha abierto el plano del museo en otra ventana. ¡Estúdialo bien!")
    except OSError:
        decir("(No se ha podido abrir la imagen del mapa)")

# Loop principal del juego
def start_game(game_state=None):
    if game_state is None:
        game_state = crear_game_state()

    decir(LETRERO)
    decir("Estás visitando el Museo del Prado y te pierdes de tus amigos.")
    decir("¡Te están enviando mensajes y dicen que te esperan en la salida!")
    decir("")
    mostrar_mapa()
    preguntar("Pulsa Enter para empezar... ")

    while game_state["current_room"] != game_state["target_room"]:
        modulo = MODULOS[game_state["current_room"]["name"]]
        decir("")
        decir(modulo.INTRO)
        game_state["current_room"] = jugar_sala(game_state, modulo.ACCIONES)

    decir("")
    decir("¡Has conseguido escapar del Museo del Prado!")


if __name__ == "__main__":
    try:
        start_game()
    except (KeyboardInterrupt, EOFError):
        print("\nHas abandonado el museo. ¡Hasta la próxima!")