# menugen_proyCF versión alfa minus 
## Diana Mendoza##
##  Archivero viral ##
Mi proyecto es una aplicación en terminal para manejar y visualizar archivos de secuencias virales. 
### Funcionalidades ###
Se trata de un menú que permite realizar algunas actividades de gestión de archivos. La particularidad es, que se utilizan secuencias de genes virales, obtenidos del GenBank 
* Enlistar documentos de archivos de secuencias virales en .txt
* Despliega el contenido del fragmento de secuencia viral
* Permite la eliminación de archivos

## Ejecutar ##
En tu terminal ejecuta la siguiente línea (recuerda tener instalado python3) y si estás en Windows, hacerlo desde tu Powersheel activando tu Ubuntu 
``python3 menugen_v2.1.py ``

## Interfaz de Terminal ##

En automático se desplegarán las siguientes opciones:
```
¿Qué secuencia quieres conocer?
A) Dime cuáles tienes 
B) Leer secuencia - automático 
C) Leer secuencia -manual 
D) Eliminar secuencia
E) Limpiar pantalla
F) Adiós

```
## Opciones del menú
* *A) Dime cuáles tienes : te enlista las secuencias que hay en el sistema*
* *B) Leer secuencia - automático : te muestra 2 secuencias (adenovirus de perro y adenovirus de pollo) *revisar áreas de oportunidad*
* *C) Leer secuencia -manual: te permite abrir secuencias en formato .txt (Virus_Canino.txt y Virus_pollo.txt) **ojo: debes ingresar [Nombre de archivo].txt**
* *D) Eliminar secuencia: te pide el nombre exacto del archivo a eliminar *
* *E) Limpiar pantalla: te ayuda a despejar tu espacio de trabajo, así como a mostrarte denuevo las opciones del menú principal*
* *F) Adiós: te da salida de la aplicación*

# Áreas de Oportunidad

* Tuve dificultad para poder darle stop al despliegue de resultados por cada opción, lo que se traduce en que se despliegan en loop interminable.
* Quise adaptar una opción automática de despliegue, metiendo un listado dentor de una de las opciones, sin mebargo, me parece que aunque tengo definidas las funciones, no lo pude llamar del todo bien en el método.
* Esta aplicación en terminal es dinámica y como perspectivas se me ocurre que pueda ser ligad al ftp o api del NCBI para descargar fragmentos de genes de interés (para este proyecto, no se descragó lasecuencia completa del virus, solo una parte de un gen de adenoviru
