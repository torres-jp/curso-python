frutas = ['manzana', 'pera', 'banana', 'frutilla', 'anana', 'naranja', 'pomelo']

longitud = len(frutas) # devuelve la cantidad de elemntos dentro de la lista

listaStrings = ['uno', 'dos', 'tres']
listaNumbers = [1,2,3,4,5]
listaBool = [True,False, False]
listaMix = ['uno',5,True]

tipo = type(listaBool)

listaDesdeConstructor = list(('Beta', 1, True))
# print(listaDesdeConstructor)

## Acceder a los datos
parteLista = frutas[1:3]
desdeComienzo = frutas[:2] # Desde el comienzo hasta el elemento 2 incluido
hastaFinal = frutas[2:] # Desde el elemento 2 hasta el final


## verificar si existe algun elemento

if 'anana' in frutas:
    print("Si esta incluido")
else:
    print("No esta en la lista")