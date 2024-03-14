import random
def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    numero = random.randint(1,10)
    print("adivina el numero")
    prediccion = int(input())
    if numero == prediccion:
        print("Correcto 👍, estás dentro del 1/10 de personas que le achuntaron")
    else:
        print(f"Incorrecto😪, el numero era {numero}")

adivinar_numero()