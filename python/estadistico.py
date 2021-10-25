# Programa estadístico básico
import math

def media():
    pass
def mediaP():
    pass



def run():
    print('''
Bienvenido! en este programa podras calcular la media (y la media ponderada) de los números que ingreses
    ''')
    calculo = input('''
Primero que todo elige que función del programa quieres usar:

a) Media normal.
b) Media ponderada.

Cuál calculo deseas realizar: ''')

    if calculo == 'a':
        result = media()
    elif calculo == 'b':
        result = mediaP()
    else:
        print('\nPor favor elige una opción válida')



if __name__ == '__main__':
    run()


#Continuará