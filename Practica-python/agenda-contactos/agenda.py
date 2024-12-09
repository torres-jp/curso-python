def mostrar_menu():
    print("\nAgenda de Contactos:")
    print("1. Agregar nuevo contacto.")
    print("2. Eliminar contacto existente.")
    print("3. Buscar contacto.")
    print("4. Lista de contactos.")
    print("5. Salir del programa.")


def agregar_contacto(agenda):
    nombre = input("Introduzca el nombre del contacto: ")
    telefono = input("Introduzca el telefono de contacto: ")
    email = input("Introduzca el email de contacto: ")

    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"Se agrego el contacto: {nombre} exitosamente")


def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} fue eliminado.")
    else:
        print(f"No se ha encontrado el {nombre}")


def buscar_agenda(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f'Telefono: {agenda[nombre]['telefono']}')
        print(f'Email: {agenda[nombre]['email']}')
    else:
        print(f"El contacto {nombre} no existe en la agenda.")


def listar_contactos(agenda):
    if agenda:
        print('\nLista de contactos: ')
        for nombre,info in agenda.items():
            print(f'Nombre: {nombre}')
            print(f'Email: {info['email']}')
            print(f'Telefono: {info['telefono']}')
            print('-' * 20)
    else:
        print('La agenda esta vacia')        



def agenda_contacto():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Eliga una opcion: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_agenda(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos!!")
            break
        else:
            print("Por favor seleccione una opcion valida (del 1 al 5)")


agenda_contacto()
