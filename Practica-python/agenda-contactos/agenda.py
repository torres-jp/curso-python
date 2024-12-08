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


def agenda_contacto():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Eliga una opcion: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("Saliendo de la agenda de contactos!!")
            break
        else:
            print("Por favor seleccione una opcion valida (del 1 al 5)")


agenda_contacto()
