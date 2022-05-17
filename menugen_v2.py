import os
from pathlib import Path
from re import A

# Ubica el directorio de trabajo de la aplicación
directorio_trabajo = Path.cwd()
ruta_actual = Path(directorio_trabajo)

def menu():
    print ('¿Qué secuencia quieres conocer?')
    print ('A) Dime cuáles tienes')
    print ('B) Revisar secuencia')
    print ('C) Eliminar secuencia') 
    print ('D) Adiós') 

# Valida que el valor ingresado por el usuario sea texto 
def validacion_opciones():
    while True:
        entrada = input('Ingrese la letra del listado, para su selección: ')
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

""" 
Muestra el contenido del secuencia .txt solitado, 
además de validar que el usuario haya ingresado el nombre de un documento existente
"""
def leer_secuencias():
    while True:
        nombre = input('¿Qué secuencia quieres conocer? (Nombre + .txt): ')
        ruta_documento = directorio_trabajo / nombre
        if ruta_documento.exists():
            with open(ruta_documento) as documento:
                archivo = documento.read()
                print(archivo)
                break
        else:
            print('El documento no existe')

"""Elimina el documento solicitado,  
además de validar que el usuario haya ingresado el nombre de un documento existente
"""
def eliminar_documento():
    while True:
        nombre = input('¿Qué archivo quiere eliminar? (Nombre + .txt): ')
        ruta_documento = directorio_actual / nombre
        if ruta_documento.exists():
            os.remove(ruta_documento)
            break
        else:
            print('El documento no existe')

"""
Valida si el usuario quiere continuar con la consulta, 
si el usuario desea continuar, la pantalla se limpia en automático,
de lo contrario termina la ejecución del programa
"""
def limpiar_pantalla():
    while True:
        continuar = (input('¿Quiere hacer otra consulta ? Si / No: '))
        if continuar.upper() == "SI":
            os.system('clear')
            break
        elif continuar.upper() == "NO":
            print('Fin de la consulta')
            exit()

menu()
eleccion = validacion_opciones()

"""
Muestra el menú en un ciclo constante hasta que el usuario decida terminar la consulta
"""
while eleccion:
    if eleccion == 'A':
        listar_secuencias()
    elif eleccion == 'B':
        leer_secuencias()
    elif eleccion == 'C':
        eliminar_documento()
    elif eleccion == D:
        print ('Fin de la consulta')
        break
    limpiar_pantalla()
    menu()
    eleccion = validacion_opciones()