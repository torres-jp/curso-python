import random


def obtener_palabra_secreta() -> str:
    palabras = [
        "python",
        "javascript",
        "java",
        "angular",
        "django",
        "react",
        "git",
        "typscript",
        "flusk",
    ]
    return random.choice(palabras)


def mostrar_progreso(palabra_secreta, letras_acertadas):
    aciertos = ""
    for letra in palabra_secreta:
        if letra in letras_acertadas:
            aciertos += letra
        else:
            aciertos += "_"

    return aciertos


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_acertadas = []
    intentos = 7
    game_over = False
    print("!Bienvenido al juego.")
    print(f"Tiene 7 {intentos} para ganar.")
    print(mostrar_progreso(palabra_secreta, letras_acertadas))

    while not game_over and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Introduzca una letra valida")
        elif adivinanza in letras_acertadas:
            print("Ya utilizaste esa letra , intenta con otra.")
        else:
            letras_acertadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"Felicitaciones , acertaste una letra {adivinanza}")
            else:
                intentos -= 1
                print(f"Lo siento la letra {adivinanza} no es la correcta")
                print(f"Te quedan: {intentos} intentos")
        
        progreso_actual = mostrar_progreso(palabra_secreta,letras_acertadas)
        print(progreso_actual)


        if '_' not in progreso_actual:
            game_over = True
            print(f'Felicidades, GANASTE, encontraste la {palabra_secreta}')


    if intentos == 0:
        print(f'Lo sentimos se acabaron los {intentos}, la palabra secreta era: {palabra_secreta} ')


juego_ahorcado()