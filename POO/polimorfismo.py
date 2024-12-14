# Clase Padre
class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        print("Hacer un sonido")


class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("La guitarra")

    # vamos a sobreescribir el metodo con un comportamiento de esta clase
    def tocar(self):
        print(f"\033[91m{self.nombre} esta haciendo mejor sonido")


class Bateria(Instrumento):
    def __init__(self):
        super().__init__("La Bateria")

    # vamos a sobreescribir el metodo con un comportamiento de esta clase
    def tocar(self):
        print(f"\033[92m {self.nombre} esta haciendo un gran ritmo ")


class Piano(Instrumento):
    def __init__(self):
        super().__init__("El Piano")

    # vamos a sobreescribir el metodo con un comportamiento de esta clase
    def tocar(self):
        print(f"\033[93m{self.nombre} esta haciendo un solo increible")


guitarra = Guitarra()
bateria = Bateria()
piano = Piano()

## POLIMORFISMO: es la capacidad de un metodo de hacer distintas cosas dependiendo de la clase origen
guitarra.tocar()
bateria.tocar()
piano.tocar()
