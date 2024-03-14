import random
opcion = input('¿El numero sera par o impar? : ')
def adivinar_par_o_impar(opcion):
    numero = random.randint(1,1000)
    if opcion == "impar" and numero%2 != 0:
        return f"wena ganaste, el numero era: {numero}"
    elif opcion == "par" and numero%2 == 0:
        return f"wena ganaste, el numero era: {numero}"
    else:
        return f"perdiste xd, el numero era: {numero}"
print(adivinar_par_o_impar(opcion))
