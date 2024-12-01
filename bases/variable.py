"""Variables
Es un contenedor para almacenar valor de datos
Este contenedor  va a tener un nombre
Es creada la primera vez que se le asigna un valor"""


x = 5
X = 6 # caseSensitive 
txt = "Esto es texto"

print(x)
print(X)
print(txt)

## nombres admitidos de variables

# Puede empezar con una letra o guion bajo (underScore)



mivariable = "texto"
_mivariable = "texto 3"
miOtravariable = """
otro texto mas
"""

_miOtravariablemas = '''
otro texto mas con comilla simples
'''

print(mivariable)
print(_mivariable)
print(miOtravariable)
print(_miOtravariablemas)


## Una variable no puede iniciar con un numero
# 5variable = "texto"
# pring(5variable)


## Solo pueden contener caracteres alfanumericos o guines bajos _
miVariable123 = "texto"
_miVariable123 = "texto 2"

### CaseSensitive ( no solo al comienzo sino en general)
miVariable = "texto"
MiVariable = "texto"

print (miVariable123)
print (_miVariable123)
print (miVariable)
print (MiVariable)

## Convenciones de escritura de variables
# camelCase
camelCase = "Comienza con minuscula y la palabra siguiente comienza en Mayuscula"

# PascalCase
PascalCase = "Comienza con Mayuscula y la palabra siguiente comienza en Mayuscula"

# Snake Case 
snake_case = "Comienza con minuscula y las palabras se unen con guion bajo"

print(camelCase)
print(PascalCase)
print(snake_case)


#########################################

# Multi-Asignacion
x,y,z = 5,7,9
print(x)
print(y)
print(z)

a = b = c = 'Texto'

print(a)
print(b)
print(c)

b = "Diferente texto"

print(b)

frutas = ['banana', 'naranja', 'frutilla']
m,n,o = frutas

print(m)
print(n)
print(o)

## use de print y salidas

txt = 'Curso '
txt2 = 'de '
txt3 = 'python '

num1 = 2
num2 = 4
num3 = 6

print(txt + txt2 +txt3) # Usando una coma (,) funciona igual solo agrega un espacio mas

print(num1+num2+num3)

print(num1 , txt3) # Usando coma (,) se puede concatenar datos numericos y string


## Variables globales vs variables de Scope
variableGlobal = "Esta variable esta disponible para todo el programa"

def function():
    global variableDeScope
    variableDeScope = "Esta variable solo funciona dentro de la funcion"
    variableGlobal = "Este valor es solo para dentro de la funcion , no afecta al valor de afuera"
    print(variableGlobal)
    print(variableDeScope)

function()

print(variableGlobal)
# print(variableDeScope) # Indefinido porque solo existe dentro de la funcion
print(variableDeScope)