# Clase: Es una plantilla que define caracteristicas y comportamiento de un objeto.
class Robot:
    #Constructor: es un metodo especial que se ejecuta al crear una instanacia y permite
    #inicializar los atributos
    #self: se refiere a la instancia especifica
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    #Metodo: es una funcion que define el comportamiento o accion de un objeto
    def saludar(self):
        print(f'Hola soy {self.nombre} y soy un robot.')

    def hacer_truco(self):
        if self.tipo == 'humanoide':
            print(f'soy {self.nombre} y ...')
        else:
            print(f'soy {self.nombre} y de tipo {self.tipo}')
    


# Instancia: que es un objeto especifico creado a partir de la plantilla llamada clase.
robotin = Robot('Megatron', 'humanoide')
tostadora = Robot('tostadora', 'electrodomestico')

#impresion
robotin.hacer_truco()
tostadora.hacer_truco()