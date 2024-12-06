# TUPLA: Coleccion ordenada e inmutable de elementos
tupla = ('a', 'b','c')

vehiculos = ('Bicicleta','Moto','Auto','Camioneta','Avion','Barco')

longitud = len(vehiculos)
tipo = type(vehiculos)
tuplaConstructor = tuple(('Esto','es','una', 'tupla'))

### Acceso por indices
elemento1 = vehiculos[1]
elemento2 = vehiculos[2]
rango = vehiculos[3:5]
desdeInicio = vehiculos[:4]
hastaFinal = vehiculos[3:]

### nueva variable que le paso una tupla
listaVehiculos = list(vehiculos)
listaVehiculos[3] = 'Camion'
listaVehiculos.append('Crucero')
vehiculos = tuple(listaVehiculos)


### Desempaquetamiento:
(a,b,c,d,e,f,g) = vehiculos # Se asigna cada elemento a una variable correspondiente a la posicion
(bici, moto, *CuatroRuedas, avion , barco , crucero) = vehiculos


### Recorrer tuplas:
for vehiculo in vehiculos:
    print(vehiculo)


for i in range(len(vehiculos)): # TUPLA
    print(f"{i+1}. {vehiculos[i]}")


[print(vehiculo) for vehiculo in vehiculos] # shorthand para una impresion de lista iterable

### JOIN  de tuplas (unir tuplas)
citricos = ('naranja', 'limon', 'pomelo')
tropical = ('papaya', 'coco', 'banana')

frutas = citricos + tropical

dobleTropical = tropical * 2
print(dobleTropical)