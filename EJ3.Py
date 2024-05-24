import os

def mostrar_linea_tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce el primer número entero entre 1 y 10 (para la tabla): "))
            if 1 <= n <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    
    while True:
        try:
            m = int(input("Introduce el segundo número entero entre 1 y 10 (para la línea): "))
            if 1 <= m <= 10:
                break
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    
    nombre_archivo = f"tabla-{n}.txt"
    
    if os.path.exists(nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                lineas = archivo.readlines()
                if 1 <= m <= len(lineas):
                    print(lineas[m-1].strip())
                else:
                    print(f"El archivo {nombre_archivo} no tiene {m} líneas.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")
    else:
        print(f"El archivo {nombre_archivo} no existe.")

mostrar_linea_tabla_multiplicar()