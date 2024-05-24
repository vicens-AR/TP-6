import os

def crear_listin():
    if not os.path.exists("listin.txt"):
        with open("listin.txt", 'w') as archivo:
            pass 
        print("Archivo listin.txt creado.")
    else:
        print("El archivo listin.txt ya existe.")

def consultar_telefono(nombre_cliente):
    if os.path.exists("listin.txt"):
        with open("listin.txt", 'r') as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split(',')
                if nombre.lower() == nombre_cliente.lower():
                    print(f"El teléfono de {nombre_cliente} es {telefono}.")
                    return
            print(f"El cliente {nombre_cliente} no está en el listín.")
    else:
        print("El archivo listin.txt no existe.")

def anadir_cliente(nombre_cliente, telefono):
    with open("listin.txt", 'a') as archivo:
        archivo.write(f"{nombre_cliente},{telefono}\n")
    print(f"Cliente {nombre_cliente} añadido con el teléfono {telefono}.")

def eliminar_cliente(nombre_cliente):
    if os.path.exists("listin.txt"):
        lineas = []
        encontrado = False
        with open("listin.txt", 'r') as archivo:
            lineas = archivo.readlines()
        
        with open("listin.txt", 'w') as archivo:
            for linea in lineas:
                nombre, telefono = linea.strip().split(',')
                if nombre.lower() != nombre_cliente.lower():
                    archivo.write(f"{nombre},{telefono}\n")
                else:
                    encontrado = True
        
        if encontrado:
            print(f"Cliente {nombre_cliente} eliminado del listín.")
        else:
            print(f"El cliente {nombre_cliente} no está en el listín.")
    else:
        print("El archivo listin.txt no existe.")

def menu():
    crear_listin()
    while True:
        print("\nGestión del Listín Telefónico")
        print("1. Consultar teléfono")
        print("2. Añadir cliente")
        print("3. Eliminar cliente")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre_cliente = input("Introduce el nombre del cliente: ")
            consultar_telefono(nombre_cliente)
        elif opcion == '2':
            nombre_cliente = input("Introduce el nombre del nuevo cliente: ")
            telefono = input("Introduce el teléfono del nuevo cliente: ")
            anadir_cliente(nombre_cliente, telefono)
        elif opcion == '3':
            nombre_cliente = input("Introduce el nombre del cliente a eliminar: ")
            eliminar_cliente(nombre_cliente)
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

menu()