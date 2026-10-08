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

# Loop principal del juego
def start_game(game_state=None):
    if game_state is None:
        game_state = crear_game_state()

    decir(LETRERO)
    decir("Estás visitando el Museo del Prado y te pierdes de tus amigos.")
    decir("¡Te están enviando mensajes y dicen que te esperan en la salida!")
    decir("")
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