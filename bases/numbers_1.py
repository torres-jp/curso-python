# int (numero entero)

numero_entero = 10

# float (numero flotante)

numero_decimal = 3.14

# complex (numero complejo con una parte imaginaria)

numero_complejo = 5 + 2j 


print(numero_entero)
print(type(numero_entero))

print(numero_decimal)
print(type(numero_decimal))

print(numero_complejo)
print(type(numero_complejo))

decimal_desde_entero = float(numero_entero)
entero_desde_decimal = int(numero_decimal)
complejo_desde_entero = complex(numero_entero)
complejo_desde_decimal = complex(numero_decimal)

print(decimal_desde_entero)
print(entero_desde_decimal)
print(complejo_desde_entero)
print(complejo_desde_decimal)


#### RANDOM

import random

aleatorio = random.randrange(1,11)

aleatorioPar = random.randrange(2,11,2)

aleatorioImpar = random.randrange(1,11,2) # empezando desde el 1 - Numero Impar

print(aleatorio)
print(aleatorioPar)
print(aleatorioImpar)
