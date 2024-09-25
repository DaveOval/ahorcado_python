import random

palabras = ["python","programacion","codicueva","hybridge","boiler"]

#funcion que obtiene una palbra aleatoria
def eleccion_de_palabra():
    return random.choice(palabras)

def generar_tablero( palabra , letras_adivinadas ):
    tablero = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_"
        tablero += " "
    return tablero

# Buclke principal del juego
while True:
    print(''''
1) Juegar ahorcado
2) Salie del juego

Elige una opcion
''')
    opcion = int(input('>'))

    if opcion == 2:
        break
    elif opcion > 0 or opcion > 2:
        print('Opcion invalida')
