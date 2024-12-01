a = 5
b = 9
c = 7


if a > b: # si cumple esta condicion hace:
    print(f'{a} es mayor que {b}') # esta linea de codigo
elif c > b:   # si no cumple la primera condicion hace:
    print(f"{c} es mayor que {b}") # esta linea de codigo
else: # si no cumplio las lineas anteriores hace:
    print(f'{a} es menor que {b} y {c} es menor que {b}') # esta linea de codigo


## ejemplo

edad = 62

if edad >= 18 and edad <= 60:
    print('Puedes entrar')
else:
    if edad  < 18:
        print('no puedes entrar')
    else:
        print('debes tener 60')



## SHORTHANDS

a = 5
b = 55

if a > b: print(f'{a} es mayor que {b}')

print('b es mayor que A') if b > a else print("a es mayor que b")

