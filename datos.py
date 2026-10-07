# ============================================================
# DICCIONARIO DE DATOS
# Sala Velázquez -> Sala de las musas -> Cafetería -> Vestuario -> Salida
# ============================================================

# Puertas
puerta_a = {"name": "puerta A", "type": "door"}   # Velázquez -> Aseo (trampa)
puerta_b = {"name": "puerta B", "type": "door"}   # Velázquez -> Sala de las musas
puerta_c = {"name": "puerta C", "type": "door"}   # Sala de las musas -> Cafetería
puerta_d = {"name": "puerta D", "type": "door"}   # Cafetería -> Vestuario
puerta_e = {"name": "puerta E", "type": "door"}   # Vestuario -> Salida

# Sala 1: Velázquez
sala_velazquez = {"name": "sala velazquez", "type": "room"}
meninas = {"name": "Las Meninas", "type": "items"}
hilanderas = {"name": "Las Hilanderas", "type": "items"}
breda = {"name": "La rendición de Breda", "type": "items"}
cartel = {"name": "Cartel de suelo mojado", "type": "items"}

# Aseo
aseo = {"name": "aseo", "type": "room"}

# Sala 2: Sala de las musas
sala_musas = {"name": "sala de las musas", "type": "room"}
carlos = {"name": "Carlos V", "type": "items", "secret_number": 3, "attempts": 2}
hipnos = {"name": "Hipnos", "type": "items"}
vigilante = {"name": "Vigilante", "type": "items",
             "correct_answer": "par", "wrong_answer": "impar"}
venus = {"name": "Venus del Delfín", "type": "items"}
vaso = {"name": "Vaso de agua", "type": "items"}

# Sala 3: Cafetería
cafeteria = {"name": "cafeteria", "type": "room"}
nevera = {"name": "nevera", "type": "items"}
mesa = {"name": "mesa 4", "type": "items"}
barra = {"name": "barra", "type": "items"}
papelera = {"name": "papelera", "type": "items"}

# Sala 4: Vestuario
vestuario = {"name": "vestuario", "type": "room"}
taquilla_28 = {"name": "taquilla 28", "type": "items", "code": "2468",
               "hint": "Numeros pares de una sola cifra"}
abrigo = {"name": "abrigo", "type": "items"}
taquilla_75 = {"name": "taquilla 75", "type": "items", "code": "13579",
               "hint": "Numeros impares de una sola cifra"}
banco = {"name": "banco", "type": "items"}

# Sala 5: Salida
salida = {"name": "salida", "type": "room"}

# Llaves
llave_a = {"name": "llave A", "type": "key", "target": puerta_a}
llave_b = {"name": "llave B", "type": "key", "target": puerta_b}
llave_c = {"name": "llave C", "type": "key", "target": puerta_c}
llave_d = {"name": "llave D", "type": "key", "target": puerta_d}
llave_e = {"name": "llave E", "type": "key", "target": puerta_e}
llave_f = {"name": "llave F", "type": "key", "target": None}   # trampa

# Pistas
pista_carlos = {"name": "pista", "type": "clue", "text": "Empieza por V"}
pista_vigilante = {"name": "pista", "type": "clue",
                   "text": "La llave está en la escultura cuyo nombre tiene 14 letras"}
pista_mesa_4 = {"name": "hoja_de_papel", "type": "clue", "text": "Frío"}

# ============================================================
# RELACIONES. La clave es SIEMPRE el "name" del elemento.
#   sala   -> lo que se ve en ella
#   objeto -> lo que contiene (llaves o pistas)
#   puerta -> las dos salas que une
# ============================================================
object_relations = {
    # Salas
    sala_velazquez["name"]: [meninas, hilanderas, breda, cartel, puerta_a, puerta_b],
    aseo["name"]: [puerta_a],
    sala_musas["name"]: [carlos, hipnos, vigilante, venus, vaso, puerta_b, puerta_c],
        cafeteria["name"]: [barra, mesa, papelera, nevera, puerta_c, puerta_d],
    vestuario["name"]: [banco, taquilla_75, abrigo, taquilla_28, puerta_d, puerta_e],

    # Contenido de los objetos
    hilanderas["name"]: [llave_a],
    cartel["name"]: [llave_b],
    carlos["name"]: [pista_carlos],
    vigilante["name"]: [pista_vigilante],
    venus["name"]: [llave_c],
    nevera["name"]: [llave_d],
    mesa["name"]: [pista_mesa_4],
    taquilla_28["name"]: [llave_e],
    abrigo["name"]: [llave_f],

    # Puertas
    puerta_a["name"]: [sala_velazquez, aseo],
    puerta_b["name"]: [sala_velazquez, sala_musas],
    puerta_c["name"]: [sala_musas, cafeteria],
    puerta_d["name"]: [cafeteria, vestuario],
    puerta_e["name"]: [vestuario, salida],
}

# ============================================================
# GAME_STATE: plantilla de inicio. NO se modifica nunca;
# cada partida trabaja sobre una copia (ver crear_game_state).
# ============================================================
INIT_GAME_STATE = {
    "current_room": sala_velazquez,
    "keys_collected": [],
    "target_room": salida,
}