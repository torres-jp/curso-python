def funcion(profesor,curso,femenino):
    profesion = 'el profesor'
    if femenino:
        profesion = 'la profesora'
    print(f'El curso de {curso} lo dara {profesion} profesor {profesor}')


funcion('Jhon Wick', 'Python', False)
funcion('Sara Connor', 'Java', True)
funcion('Sara Connor', 'C++', False)
funcion('Sara Connor', 'Ruby', True)


### Variables por defecto
def decir_pais(pais = 'Argentina'):
    print(f'El nombre de mi pais es: {pais}')

decir_pais('Mexico')


### Retornar valores
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b


def multiplicacion(a,b):
    return a * b

    
def division(a,b):
    return a // b



resultado_suma = suma(5,5)
resultado_resta = resta(5,3)
resultado_division = division(10,2)
resultado_multiplicacion = multiplicacion(4,2)

print(resultado_suma)
print(resultado_resta)
print(resultado_division)
print(resultado_multiplicacion)


### Argumentos arbitrarios
def llamar_alumnos(*alumnos):
    print(f'Mi mejor alumno es {alumnos[0]}')
    print(f'Mi peor alumno es {alumnos[2]}')


llamar_alumnos('Peter', 'Jhon', 'Sarah', 'Mary')


### Argumento clave
def cursos(curso1, curso2, curso3):
    print(f"El primer curso que se toma es {curso1}")
    print(f"El segundo curso que se toma es {curso3}")
    print(f"El ultimo curso que se toma es {curso3}")


cursos(curso3="Java", curso2="C++", curso1="HTML")


### Argumentos claves arbitrarios
def llamar_alumno(**alumno):
    print(f'El apellido del alumno es {alumno['apellido']}, y si nombre es {alumno['nombre']}')

llamar_alumno(apellido = 'Wick', nombre = 'Jhon', edad = 33)


### Otros tipos de datos
lista = ['JavaScript', 'Python', True, 88]
number = 33

def usar_tipos_de_datos(lista, number):
    print(lista)
    print(number)

usar_tipos_de_datos(lista, number)
usar_tipos_de_datos(['Ruby', False],2)


### Recursividad 
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)    


numero = 3
print(f'El factorial de: {numero} es {factorial(numero)}')        