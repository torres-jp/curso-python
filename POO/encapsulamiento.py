class Cajafuerte:
    def __init__(self, clave, cantidad):
        self.__clave = clave
        self.__cantidad = cantidad

    # getters metodos para obtener informacion de los atributos privados.
    # def obtener_clave(self):
    #     return self.__clave

    def verificarClave(self, clave):
        return (
            self.__clave == clave
        )  # Devolvera TRUE si la clave coinside con la original

    def obtener_cantidad(self, clave):
        if self.verificarClave(clave):
            return self.__cantidad
        else:
            print("La clave no es correcta")

    # setters son metodos para establecer nuevos valores a los atributos privados.
    def establecer_clave(self, clave_nueva, clave):
        if self.verificarClave(clave):
            if len(clave_nueva) < 4:
                print("La clave debe tener al menos 4 caracteres")
            else:
                print('La clave fue cambiada')
                self.__clave = clave_nueva
        else:
            print("La clave no es correcta")

    def establecer_cantidad(self, canitdad_nueva, clave):
        if self.verificarClave(clave):
            if canitdad_nueva <= 0:
                print("No se puede colocar una cantidad negativa")
            else:
                print('La cantidad fue cambiada')
                self.__cantidad = canitdad_nueva
        else:
            print('La clave no es correcta')

caja = Cajafuerte("1234", 1000)


print(caja.obtener_cantidad("1234"))

caja.establecer_clave('4567','1234')
caja.establecer_cantidad(3500,'4567')
print(caja.obtener_cantidad('4567'))