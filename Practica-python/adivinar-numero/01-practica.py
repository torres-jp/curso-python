import random


def adivinar():
    # generar un numero del 1 al 100
    numero_secreto = random.randint(1, 10)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego")

    while not adivinado:
        intento = input("Introducir numero: ")

        if intento.isdigit():
            intento = int(intento)
            intentos += 1

            if intento < numero_secreto:
                print(f"El numero es mayor a {intento}")
            elif intento > numero_secreto:
                print(f'El numero es menor a {intento}')
            else:
                print(f'Felicitaciones Ganaste, el Numero era {intento} y lo lograste en: {intentos} intentos')
        else:
            print('Por favor ingrese un numero valido')         


adivinar()