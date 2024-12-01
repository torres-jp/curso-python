# str (string) cadena de caracteres
comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = """Este es un texto"""
comillasTriplesSimples = '''Este es un texto'''

# int (integer) numero entero
numero_entero = 22

# float (decimal) numero decimal
numero_decimal = 3.14

# complex (complejo) numero complejo parte entera y parte imaginaria
numero_complejo = 5 + 2j

# list[] (lista) coleccion ordenada y mutable de elementos
lista = [0,1,2,3,4,5]

# tuple() coleccion ordenada e inmutable de elemntos
lista = (0,1,2,3,4,5)

# range Una secuencia de numeros generada dentro de un rango
rango = range(1,10)

# dict (dictionary) coleciones de pares desordenada y mutable
diccionario = {
    "nombre": "jhon",
    "edad": 5,
    "diccionario2": {
        "apellido": "wick"
    }
}


# set{} coleccion desordenada de elementos unicos y mutables
conjunto = { 1,1,2,3,4,5,5,6}

print(conjunto)

# frozenSet([]) coleccion desordenada de elementos unicos e inmutables
conjunto_inmutable = frozenset([1,2,3,3,3])

# bool (boolean)
correcto = True
incorrecto = False