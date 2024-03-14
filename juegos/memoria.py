import random
def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    print("ELIGE LA DIFICULTAD (FACIL, NORMAL, DIFICIL, JORGE)")
    dificultad = str(input()).upper()
    if dificultad == "FACIL":
        longitud = random.randint(2,4)
    elif dificultad == "NORMAL":
        longitud = random.randint(5,7)
    elif dificultad == "DIFICIL":
        longitud = random.randint(8,10)
    elif dificultad == "JORGE":
        longitud = random.randint(11,20)
    else:
        print("pusiste mal la dificultad...")
        longitud = random.randint(20,30)

    print("RECUERDA ESTOS NUMEROS!!!!")
    lista1 = ""
    lista2 = ""
    for i in range(longitud):
        numero = random.randint(0,9)
        lista1 += str(numero) + ","
        lista2 += str(numero)
    lista1 = lista1[:len(lista1)-1]
    print(lista1)
    print("Apreta Enter para comenzar")
    pregunta = input()
    for i in range(20):
        print(".\n\n\n\n")
    print("Escribe los numeros")

    intento = str(input())

    while (intento != lista1) and (intento != lista2):
        print("Nop, inténtalo de nuevo")
        intento = str(input())

    print("Lo lograste, tienes muy buena memoria")

memoria()