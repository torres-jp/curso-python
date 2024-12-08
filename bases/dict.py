dicc = {
    "name": "jhon",
    "lastname": "wick",
    "lenguajes": ["python", "java", "ruby"],
    "age": 33,
    "adress": {"street": "Av Siempre-viva", "number": 3243, "country": "Brazil"},
}

tipo = type(dicc)
longitud = len(dicc)
constructorDicc = dict(name = 'jhon', lastname = 'wick')

nombre = dicc['name']
keys = dicc.keys()
values = dicc.values()
items = dicc.items() # devuelve una tupla dentro de una lista.


if "age" in dicc: # comprobar si existe la keys
    print('Existe la key en el diccionario')


### Cambio de values en el dict
dicc['lenguajes'] = ['Python', 'Java', 'Node', 'Ruby']
dicc.update({"age": "38"})

## Agregar items
dicc['email'] = "email@example.com"
dicc.update({'user': 'user123'})


## Eliminar items
dicc.pop('user') # elimina el ultimo elemento
dicc.popitem() # elimina ultima caracteristica agregada
del dicc['age']
dicc.clear() # vacia todo el dict


### Bucles

curso_python = {
    "nombre": "curso python",
    "duracion": 9,
    "dificultad": "media",

}

for key in curso_python: # el bucle for devuelve las keys
    print(f'{key.upper()}: {curso_python[key]}')


for x in curso_python.values():
    print(x)

for x,y in curso_python.items():
    print(f'{x}:{y}')

### Copiar dict
copia = curso_python.copy() # copia exacta pero apunta a otra direccion de memoria
copia2 = dict(curso_python) # copia usando constructor

### Dict anidados
hijo1 = {
    "nombre": "peter",
    "edad": "5"
}

hijo2 = {
    "nombre": "pedro",
    "edad": "8"
}

hijo3 = {
    "nombre": "perro",
    "edad": "12"
}

familia = {
    "hijo1": hijo1,
    "hijo2": hijo2,
    "hijo3": hijo3,
}

edad2 = familia['hijo2']['edad']

for x,obj in familia.items():
    print(x)
    for y in obj:
        print(f'{y.capitalize()}: {obj[y]}') 