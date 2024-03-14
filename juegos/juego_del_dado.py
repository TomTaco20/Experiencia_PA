import random
def juego_del_dado():
    jp= 0
    pc= 0
    while jp <30 or pc < 30:
        if jp <= 30 or pc <= 30:
            n1=random.randint(1,6)
            jp+= n1
            print(f'{n1} valor del dado del jugador. Puntaje actualjugador: {jp}')
            n2=random.randint(1,6)
            pc+= n2
            print(f'{n2} valor del dado de la computadora. Puntaje actual PC: {pc}')
            if jp >= 30:
                return(print(f'Has ganado con {jp} puntos'))
            elif pc >= 30:
                return(print(f'Ha ganado el pc con {pc} puntos'))
    return('elpepe')
input('Presiona Enter para comenzar')
juego_del_dado()

