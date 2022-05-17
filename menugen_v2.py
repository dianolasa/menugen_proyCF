import os
from pathlib import Path


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
            print ("La entrada es incorrecta; escribe una letra que esté en el lista")

# Muestra las secuencias existentes, con extensión .txt
def listar_secuencias():
    for secuencia in ruta_actual.iterdir():
    
        if secuencia.is_file() and  secuencia.suffix == '.txt':
            print(secuencia.name)

#Lee la lectura de la secuencia de interés
def leer_secuencias():
    while True:
        nombre = input('¿Qué secuencia quieres conocer? indica (Nombre + .txt): ')
        ruta_documento = directorio_trabajo / nombre
        if ruta_documento.exists():
            with open(ruta_documento) as documento:
                archivo = documento.read()
                print(archivo)
                break
        else:
            print('El documento no existe')

#Elimina el archivo de secuencia deseado
def eliminar_secuencia():
    while True:
        nombre = input('¿Qué secuencia quieres eliminar? (Nombre + .txt): ')
        ruta_secuencia = ruta_actual / nombre
        if ruta_secuencia.exists():
            os.remove(ruta_documento)
            break
        else:
            print('El documento no existe')

#Limpia la pantalla para visualizar secuencias
def limpiar_pantalla():
    while True:
        continuar = (input('¿Quiere revisar otra secuencia ? S / N: '))
        if continuar.upper() == "S":
            os.system('clear')
            break
        elif continuar.upper() == "N":
            print('Adiós')
            exit()

menu()
eleccion = validacion_opciones()

#Ciclo del menú
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
