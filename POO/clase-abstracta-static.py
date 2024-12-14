# Clase Abastracta: la plantilla o modelo de las clases que las heredan
from abc import ABC, abstractmethod


class Animal(ABC):
    # Atributo Estatico: va a estar disponible independientemente de las instancias
    cantidad_de_animales = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Animal.cantidad_de_animales += 1


    @abstractmethod
    def hacer_sonido(self):
        pass


    # Metodo de clase (METODO ESTATICO)
    # cls: se refiere a la clase (Al ser un atributo estatico le pertenece a la clase  y no a la instancia)
    @classmethod
    def obtener_cant_animales(cls):
        print(f'La cantidad actual de animales es: {cls.cantidad_de_animales}')




class Perro(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} hace Guau Guau')
    def mover_cola(self):
        print(f'{self.nombre} esta moviendo la colita')



class Gato(Animal):
    def hacer_sonido(self):
        print(f'{self.nombre} hace Miau Miau!')
    def ronronea(self):
        print(f'{self.nombre} ronronea')

perrito = Perro('Manchita')
gatito = Gato('Bigote')

perrito.mover_cola()
gatito.ronronea()

Animal.obtener_cant_animales()