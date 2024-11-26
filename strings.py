# str (string) cadena de caracteres

texto = "Este es un curso de python desde 0"

comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = """Este es un texto"""
comillasTriplesSimples = '''Este es un texto'''

### type
# print(type(comillasSimples))

### Arrays de caracteres

caracter = texto[2]
# print(caracter)

# len -- length
largo = len(texto)
# print(largo)

# In -- Para saber si esta incluido en el texto
# print("Python" in texto) #caseSensitive
# print("python".lower() in texto.lower())

# Not in
print("C++" not in texto)