## Clase padre
class Personajes:
    def __init__(self,nombre,poder):
        self.nombre = nombre
        self.poder = poder

    def presentarse(self):
        print(f'Hola soy {self.nombre} y mi poder es {self.poder}')


## Clase heredada
class Superheroe(Personajes):
    def salvar_el_dia(self):
        print(f'{self.nombre} esta salvando el dia usando su  {self.poder}')

class Villano(Personajes):
    def plan_malvado(self):
        print(f'Cuidado {self.nombre} esta haciendo el mal usando su poder {self.poder}')



heroe = Superheroe('Captian comando', 'lanzallamas')
villano = Villano('Blood', 'Super-velocidad')


heroe.presentarse()
villano.presentarse()


heroe.salvar_el_dia()
villano.plan_malvado()