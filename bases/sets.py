### SETS: Coleccion desordenada de elementos unicos y mutables (NO PERMITE DUPLICADOS)
conjunto = { 1,2,3,3,4,5,6,6,7} # los elementos que esten duplicados se OMITEN

longitud = len(conjunto)
tipo = type(conjunto)
constructor = set(('Este', 'es', 'un','conjunto')) # Devuelve el conjunto desordenado.

if 'conjunto' in constructor: # se puede usar in para saber si un elemento existe en el set
    print('Si existe')

if 'python' not in constructor:
    print('python no se encuentra')

### Agregar
telefonos = {'Xiaomi', 'Motorola', 'Samsung'}
telefonos2 = {'Iphone', 'ZTE', 'Huawei'}
telefonos.add('Nokia') # Agregar un elemento

telefonos.update(telefonos2) # Con update sumamos otra coleccion(lista , array)

### Eliminar
autos = {'Ford', 'Fiat', 'Mercedes', 'BMW', 'PEUGOT'}
autos.remove('Fiat') # Debe existir el elemento para ser borrado o produce un error.
autos.discard('BMW') # No es necesario que exista el elemento para ser borrado.
autos.pop() # Elimina un elemento de forma Aleatoria.
autos.clear() # Vacia la lista

### Recorrer Elementos 


lenguajes = {'python', 'c++', 'java', 'ruby'}

for lenguaje in lenguajes:
    print(lenguaje)

[print(lenguaje) for lenguaje in lenguajes] # shorthand para una impresion de lista iterable


### JOIN conjuntos # devuelve todos los elementos de ambos conjuntos
a = {1,2,3,4,5}
b = {1,3,5,7,9}

booleanos = {True, False}

## union
u = a.union(b)
uu = a | b # Exactamente lo mismo que usar "Union"

## interseccion # devuelve los en comun de ambos conjuntos
i = a.intersection(b)
ii = a & b # Exactamente lo mismo que usar 'Intersection'

# a.intersection_update(b) # intersection update modifica el conjunto original

## comportamiento con booleans
booleanos_union = a.union(booleanos)
booleanos_intersection = a.intersection(booleanos)

## diferencias 
d = a.difference(b)
d1 = a - b
dd = b.difference(a)

## diferencia simetrica , devuelve los elementos que no esten en ambos conjuntos
ds1 = a.symmetric_difference(b)
ds2 = a ^ b