## Clase padre
class Personajes:
    def __init__(self,nombre,poder):
        self.nombre = nombre
        self.poder = poder

    def presentarse(self):
        print(f'Hola soy {self.nombre} y mi poder es {self.poder}')


## Clase heredada
class Superheroe(Personajes):
    def __init__(self, nombre, poder,ciudad):
        super().__init__(nombre, poder) # Usamos super para pasarle informacion al padre.
        self.ciudad = ciudad

    def salvar_la_ciudad(self):
        print(f'{self.nombre} esta salvando la {self.ciudad}  usando su  {self.poder}')

class Villano(Personajes):
    def __init__(self, nombre, poder,archienemigo):
        super().__init__(nombre, poder)
        self.archienemigo = archienemigo


    def plan_malvado(self):
        print(f'Cuidado {self.nombre} esta haciendo el mal contra {self.archienemigo} usando su poder {self.poder}')



heroe = Superheroe('Captian Comando', 'lanzallamas', 'Metro-city')
villano = Villano('Blood', 'Super-velocidad', 'Capitan Comando')


heroe.presentarse()
villano.presentarse()


heroe.salvar_la_ciudad()
villano.plan_malvado()