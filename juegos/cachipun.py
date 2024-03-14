import random
jugada = input("Vamos a jugar al cachipun, veamos si puedes vencer a una computadora (si pierdes seras reemplazado por una), elige entre piedra, papel o tijera : ")
def cachipun(jugada):
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """
    jugadas_pc = ["piedra","papel","tijera"]
    eleccion_pc = random.randint(0,2)
    if jugada == jugadas_pc[eleccion_pc]:
        return "uff, empate, te haz salvado"
    elif jugadas_pc[eleccion_pc] == "papel":
        return "haz perdido, ahora moriras (en realidad no)"
    elif jugadas_pc[eleccion_pc] == "tijera":
        return "felicidades, haz ganado, no serás reemplazado por una IA"
    