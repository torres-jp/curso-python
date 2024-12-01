# str (string) cadena de caracteres


texto = "Este es un curso de python desde 0"

comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto"
comillasTriples = """Este es un texto"""
comillasTriplesSimples = '''Este es un texto'''

## type
print(type(comillasSimples))

## Arrays de caracteres

caracter = texto[2]
# print(caracter)

### len -- length
largo = len(texto)
print(largo)

## In -- Para saber si esta incluido en el texto
print("Python" in texto) #caseSensitive
print("python".lower() in texto.lower())

 ### Not in
print("C++" not in texto)

## Slice (cortar)
print(texto[10:16])
print(texto[:5])

## Modificadores
mayusculas = texto.upper()
print(mayusculas)

minusculas = texto.lower()
print(minusculas)

texto_con_espacios = "             hola mundo      "
texto_con_comas = "no , se olviden , de , esta"


sin_espacios = texto_con_espacios.strip()
print(sin_espacios)

remplazo = texto_con_espacios.replace("mundo", "anaconda").strip()
print(remplazo)

separar_con_comas = texto_con_comas.split(',')
print(separar_con_comas)


## Concatenar
a = 'mundo'
b = 'hola'

c = b + " " + a
print(c)


## F-Strings (template strings) 
num = 5
variable = "edad"
txt = f"la {variable} de jhon es de {num}"

print(txt)


resultado = f"El resultado de 69 x 75 es: {69*75}"
print(resultado)


## Escapes
escape = "Mi pais Favorito es \"APALATA\" porque si y algo mas"
directorio = "El directiorio de la descarga es c:\\descargas\\python.txt"
salto = "quiero hacer un \n salto de linea"
print(escape)
print(directorio)
print(salto)

texto_a_modificar = "Este es Un TexTo A ModIFIcAR"
capitalizado = texto_a_modificar.capitalize()
estaComenzando = texto_a_modificar.startswith('es') #CaseSensitive
estaFinalizando = texto_a_modificar.endswith('ModIFIcAR') #CaseSensitive
titulo = texto_a_modificar.title()
print(estaComenzando)
print(titulo)
contador = texto_a_modificar.count('e')
print(contador)
buscar = texto_a_modificar.find('TexTo')
print(buscar)