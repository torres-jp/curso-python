### SETS: Coleccion desordenada de elementos unicos y mutables (NO PERMITE DUPLICADOS)
conjunto = { 1,2,3,3,4,5,6,6,7} # los elementos que esten duplicados se OMITEN

longitud = len(conjunto)
tipo = type(conjunto)
constructor = set(('Este', 'es', 'un','conjunto')) # Devuelve el conjunto desordenado.

# if 'conjunto' in constructor: # se puede usar in para saber si un elemento existe en el set
#     print('Si existe')

# if 'python' not in constructor:
#     print('python no se encuentra')

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