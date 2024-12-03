lenguajes = ['python', 'java', 'c++', 'javaScript', 'angular', 'redux', 'Ruby', 'Django']

x = 1

texto = 'No olvidar de las sangrias dentro del codigo'

for lenguaje in lenguajes:
    if lenguaje == 'Ruby':
        break

    if lenguaje == 'redux':
        continue

    print(f'{x}. {lenguaje}')
    x += 1
else: 
    print('Son los lenguajes a estudiar.')


for caractere in texto:
    print(caractere)


for x in range(5):
    print(x)

for x in range(2,20,2):
    print(x)


letras = ['a','b','c']
numeros = [1,2,3]

for letra in letras:
    for numero in numeros:
        print(letra,numero)