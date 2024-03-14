import random
def juego_del_dado():
    jp= 0
    pc= 0
    while jp <30 or pc < 30:
        if jp <= 30 or pc <= 30:
            n1=random.randint(1,6)
            jp+= n1

            n2=random.randint(1,6)
            pc+= n2
            if jp >= 30:
                return(print('Has ganado!'))
            elif pc >= 30:
                return(print('Ha ganado el pc!'))
    return('elpepe')
input('Presiona Enter para comenzar')
juego_del_dado()

