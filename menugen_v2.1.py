from optparse import Option
import os
from pathlib import Path
from re import A
from tracemalloc import stop

# Ubica el directorio de trabajo de la aplicación
directorio_trabajo = Path.cwd()
ruta_actual = Path(directorio_trabajo)

def menu():
    print ('¿Qué secuencia quieres conocer?')
    print ('A) Dime cuáles tienes')
    print ('B) Leer secuencia - automático')
    print ('C) Leer secuencia -manual')
    print ('D) Eliminar secuencia') 
    print ('E) Limpiar pantalla') 
    print ('F) Adiós')

# Valida que el valor ingresado por el usuario sea texto 
def validacion_opciones ():
    while True:
        entrada = input('Ingresa la letra del listado, para tu selección: ')
        try:
            entrada = str (entrada)
            return entrada;
        except ValueError:
            print ("La entrada es incorrecta; escribe una letra")

# Muestra los documentos existentes con extensión .txt
def listar_secuencias():
    for secuencia in ruta_actual.iterdir():
    
        if secuencia.is_file() and  secuencia.suffix == '.txt':
            print(secuencia.name)
stop

def leer_secuencias():
    print ('1) Virus canino')
    print ('2) Virus de pollo')
stop

def validacion_secuencias():
    while True:
        entrada = input('Ingrese el número de la opción: ')
        try:
            entrada = int(entrada)
            return entrada;
        except ValueError:
            print ("La entrada es incorrecta; escribe un numero entero")

def leer_perro():
    while True:
        nombre = Virus_canino.txt
        ruta_documento = ruta_actual / nombre
        if ruta_documento.exists():
            with open(ruta_documento) as documento:
                archivo = documento.read()
                print(archivo)
                break
        else:
            print('El documento no existe')

def leer_pollo():
    while True:
        nombre = Virus_pollo.txt
        ruta_documento = ruta_actual / nombre
        if ruta_documento.exists():
            with open(ruta_documento) as documento:
                archivo = documento.read()
                print(archivo)
                break
        else:
            print('El documento no existe')
            


def ingreso_manual():
    while True:
        nombre = input('¿Qué archivo quiere leer? (Nombre + .txt): ')
        ruta_documento = ruta_actual / nombre
        if ruta_documento.exists():
            with open(ruta_documento) as documento:
                archivo = documento.read()
                print(archivo)
                break
        else:
            print('El documento no existe')

def eliminar_documento():
    while True:
        nombre = input('¿Qué archivo quiere eliminar? (Nombre + .txt): ')
        ruta_documento = ruta_actual / nombre
        if ruta_documento.exists():
            os.remove(ruta_documento)
            print("Archivo eliminado")
            limpiar_pantalla()
        else:
            print('El documento no existe')

def menu2():
    print ('¿Qué secuencia quieres conocer?')
    print ('A) Dime cuáles tienes')
    print ('B) Leer secuencia - automático')
    print ('C) Leer secuencia -manual')
    print ('D) Eliminar secuencia') 
    print ('E) Adiós') 

menu2()
eleccion = validacion_opciones()
while eleccion:
    if eleccion == 'A':
        listar_secuencias()
        
    elif eleccion == 'B':
        leer_secuencias()
    elif eleccion == 'C':
        ingreso_manual()
    elif eleccion == 'D':
        eliminar_documento()
    elif eleccion == "E":
        print ('Adiós, nos vemos')
        exit()

def limpiar_pantalla():
    while True:
        continuar = (input('¿Quiere hacer otra consulta ? Si [S] / No [N]: '))
        if continuar.upper() == "S":
            menu2()
        elif continuar.upper() == "N":
            print('Adiós')
            exit()

menu()
eleccion = validacion_opciones()
while eleccion:
    if eleccion == 'A':
        listar_secuencias()
        break
    elif eleccion == 'B':
        leer_secuencias()
    elif eleccion == 'C':
        ingreso_manual()
    elif eleccion == 'D':
        eliminar_documento()
    elif eleccion == "E":
        limpiar_pantalla()
    elif eleccion == "F":
        print ('Adiós, nos vemos')
        exit()
    break
limpiar_pantalla()



leer_secuencias()
option = validacion_secuencias()
while option:
    if option == 1:
        leer_perro()
    elif option == 2:
        leer_pollo()
    limpiar_pantalla()
option = validacion_secuencias()
