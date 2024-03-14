import random
jugada = input("Vamos a jugar al cachipun, veamos si puedes vencer a una computadora (si pierdes seras reemplazado por una), elige entre piedra, papel o tijera : ")
def cachipun(jugada):
    jugadas_pc = ["piedra","papel","tijera"]
    eleccion_pc = random.randint(0,2)
    if jugada == jugadas_pc[eleccion_pc]:
        return "uff, empate, te haz salvado"
    elif jugada == "piedra":
        if jugadas_pc[eleccion_pc] == "papel":
            return f"perdiste, jugada computadora: {jugadas_pc[eleccion_pc]}"
        elif jugadas_pc[eleccion_pc] == "tijera":
            return f"ganaste, jugada computadora: {jugadas_pc[eleccion_pc]}"
    elif jugada == "papel":
        if jugadas_pc[eleccion_pc] == "tijera":
            return f"perdiste, jugada computadora: {jugadas_pc[eleccion_pc]}"
        elif jugadas_pc[eleccion_pc] == "piedra":
            return f"ganaste, jugada computadora: {jugadas_pc[eleccion_pc]}"
    elif jugada == "tijera":
        if jugadas_pc[eleccion_pc] == "piedra":
            return f"perdiste, jugada computadora: {jugadas_pc[eleccion_pc]}"
        elif jugadas_pc[eleccion_pc] == "papel":
            return f"ganaste, jugada computadora: {jugadas_pc[eleccion_pc]}"
print(cachipun(jugada))
    
    