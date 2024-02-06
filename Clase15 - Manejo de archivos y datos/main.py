"""CLASE 15"""
name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
# ----- Persistencia de Datos ----- #
f = open("C:/Users/EQUIPO/Desktop/Python-Coder/Clase15 - Manejo de archivos y datos/datos.txt", "a")
f.write(name)
f.write(str(age)) #Al momento de escribirlo tiene que ser str
f.close

# ------ Escritura de Archivos  ------ #
from registro import * 
database = {}
user, password = userRegister(database)
getDB(database)
#Raw string
file = open(r"C:\Users\EQUIPO\Desktop\Python-Coder\Clase15 - Manejo de archivos y datos\database.txt", "a")
file.write(f"User: {user} --- Password: {password} \n")
file.close() #Cerrar siempre un archivo despues de abrirlo

# ------ Lectura de Archivos  ------ #
f = open(r"C:\Users\EQUIPO\Desktop\Python-Coder\Clase15 - Manejo de archivos y datos\dataFutbol.txt", "r") #Modo Lectura
datos = f.read() #Leyendo arch, y vamos a guardarlo en una variable
#datos = f.read(15) #Datos: Cristian
print(datos)
f.close()
print("\n")
#Leer el archivo en una sola linea
f = open(r"C:\Users\EQUIPO\Desktop\Python-Coder\Clase15 - Manejo de archivos y datos\dataFutbol.txt", "r") #Modo Lectura
datos = f.readlines() #readline() => lee solo la primera linea de un archivo
print(datos)
#Alterar datos de un arch
posicion = datos[5]
print(posicion.upper())
f.close()