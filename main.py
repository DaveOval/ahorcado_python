ahorcado_3_vidas = [
    ''' 
     -----
     |   |
         |
         |
         |
         |
    ========
    ''',
    ''' 
     -----
     |   |
     O   |
         |
         |
         |
    ========
    ''',
    ''' 
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    ''',
    ''' 
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    '''
]

ahorcado_5_vidas = [
    ''' 
     -----
     |   |
         |
         |
         |
         |
    ========
    ''',
    ''' 
     -----
     |   |
     O   |
         |
         |
         |
    ========
    ''',
    ''' 
     -----
     |   |
     O   |
     |   |
         |
         |
    ========
    ''',
    ''' 
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ========
    ''',
    ''' 
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========
    ''',
    ''' 
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========
    '''
]

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
# Seleccionamos una palabra aleatoria
palabra_secreta = eleccion_de_palabra()

# Definir el numero de vidas que tendra el usuario
tamanio_palabra = len(palabra_secreta)

# Contendra las letras que mi usuario haya adivinado
letras_adivinadas = []

#Palabra que determine si nuestro usuario ya adivino la palabra
palabra_adivinada = False

#Determinamos la cantidad de vidas de nuestro usuario en funcion del tamaño de la palabra
if tamanio_palabra > 4:
    numero_vidas = 5
    ahorcado = ahorcado_5_vidas
elif tamanio_palabra < 5:
    numero_vidas = 3
    ahorcado = ahorcado_3_vidas

print("-------------BIENVENIDO---------------")

# Buclke principal del juego
while True:
    print("\n" * 10)

    print(numero_vidas)

    print(ahorcado[numero_vidas])

    print(generar_tablero(palabra_secreta, letras_adivinadas))

    intento_usuario = input("Ingrese una letra: ").lower()

    if intento_usuario in palabra_secreta and intento_usuario not in letras_adivinadas:
        letras_adivinadas.append(intento_usuario)
    else:
        numero_vidas = numero_vidas - 1

# falta agregar las palabras con varias letras
    if numero_vidas == 0:
        print("Fin del juego te quedaste sin vidas")
        print(f"La palabra era: {palabra_secreta}")
        print(f"Has adivinado {letras_adivinadas}")
        break