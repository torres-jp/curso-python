### SINTAXIS
#lambda argunmentos1,argumento2 : return

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b


def multiplicacion(a,b):
    return a * b

    
def division(a,b):
    return a // b

# Ejemplos
def suma_lambda(a, b):
    return a + b

suma_resta = lambda a,b : a - b
suma_multiplicacion = lambda a,b : a * b
suma_division = lambda a,b : a // b



def multiplicador(n):
    return lambda a : a * n


duplicador = multiplicador(2)
print(duplicador(22))


numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)