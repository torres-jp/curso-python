######### OPERADORES


## operadores aritmeticos

a = 10
b = 5

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b # devuelve un FLoat (decimal)
floorDivision = a // b # devuelve un Int (entero)
resto = a % b # resto de la division
exponente = a ** b


## operadores por asignacion

x = 10 
x += 3 # le suma el valor a la variable llamada
x -= 2 # resta el valor a la variabale llamada
x *= 2 # multiplica el valor a la variable llamada
x /= 2 # divide el valor a la variable llamada

## operadores de comparacion

num1 = 5
num2 = 4

igualdad = num1 == num2 # devuelve True si los valores son iguales
distintos = num1 != num2  # devuelve True si los valores son distintos
mayor = num1 > num2  # devuelve True si un valor es mayor
menor = num1 < num2 # devuelve True si un valor es menor
mayorIgual = num1 >= num2 # devuelve True si un valor es mayor o igual
menorIgual = num1 <= num2 # devuelve True si un valor es menor o igual
 
## operadores logicos (and , or , not)

edad = 17
tramite = edad >= 18 and edad >= 65 # si usamos AND debe cumplir las 2 condiciones

semaforo = "Rojo"
cruzar = semaforo == "Verde" or semaforo == "Amarillo" # si usamos OR debe cumplir 1 de las condiciones


verdad = True
print(not verdad)
