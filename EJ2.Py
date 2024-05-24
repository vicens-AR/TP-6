import os

def mostrar_tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    
    nombre_archivo = f"tabla-{n}.txt"
    
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print(contenido)
    else:
        print(f"El archivo {nombre_archivo} no existe.")

mostrar_tabla_multiplicar()