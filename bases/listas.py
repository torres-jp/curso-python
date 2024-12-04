frutas = ['manzana', 'pera', 'banana', 'frutilla', 'anana', 'naranja', 'pomelo']

longitud = len(frutas) # devuelve la cantidad de elemntos dentro de la lista

listaStrings = ['uno', 'dos', 'tres']
listaNumbers = [1,2,3,4,5]
listaBool = [True,False, False]
listaMix = ['uno',5,True]

tipo = type(listaBool)

listaDesdeConstructor = list(('Beta', 1, True))
# print(listaDesdeConstructor)

## ACCEDER A LOS DATOS
parteLista = frutas[1:3]
desdeComienzo = frutas[:2] # Desde el comienzo hasta el elemento 2 incluido
hastaFinal = frutas[2:] # Desde el elemento 2 hasta el final


## verificar si existe algun elemento

# if 'anana' in frutas:
#     print("Si esta incluido")
# else:
#     print("No esta en la lista")


lenguajes = ['python', 'Java', 'c++', 'javaScript','ruby']

lenguajes[3] = 'React'
lenguajes[2:4] = ['numPy', 'Scrappy']
lenguajes.insert(2,'c++') # inserta un dato en el lugar asignado
lenguajes.append('ReactPy') # agrega un elemento a la lista


frontEnd = ['React', 'Angular', 'Vue', 'Nextjs']
lenguajes.extend(frontEnd)

# lenguajes.remove('Java')
# lenguajes.pop() # elimina el ultimo dato de la lista.

# del lenguajes[5]
# lenguajes.clear() # vacia la lista.


## RECORRER LISTAS

# for lenguaje in lenguajes:
#     print(lenguaje)


# for i in range(len(lenguajes)):
#     print(f"{i+1}. {lenguajes[i]}")


# [print(lenguaje) for lenguaje in lenguajes] # shorthand para una impresion de lista iterable

# listaconY = []

# for lenguaje in lenguajes:
#     if 'y' in lenguaje:
#         listaconY.append(lenguaje)

# print(listaconY)


# listaconY2 = [lenguaje.upper() for lenguaje in lenguajes if 'y' in lenguaje]
# print(listaconY2)


## ORDENAR UNA LISTA
lenguajes.sort()
print(lenguajes)