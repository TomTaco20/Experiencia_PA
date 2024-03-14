import random
opcion = input('¿El numero sera par o impar? : ')
def adivinar_par_o_impar(opcion):
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    numero = random.randint(1,1000)
    if opcion == "impar" and numero%2 != 0:
        return f"wena ganaste, el numero era: {numero}"
    elif opcion == "par" and numero%2 == 0:
        return f"wena ganaste, el numero era: {numero}"
    else:
        return f"perdiste xd, el numero era: {numero}"
print(adivinar_par_o_impar(opcion))
