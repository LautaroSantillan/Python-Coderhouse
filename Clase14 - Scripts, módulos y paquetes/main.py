#Módulos = Archivo
#Paquete - Carpeta de varios modulos
import definiciones.herencia as herencia #Lee el archivo llamado herencia
from definiciones.operaciones import sumar #Lee el archivo y se trae una función en especifico


print("Inicio del Programa:\nCreamos un cetáceo")
#La clase Cetaceo se encuentra dentro del archivo "herencia"
ballena = herencia.Cetaceo(2, 1, "No", "Cachalote", "Odontoceto más grande", "Oceano Pacífico", 13000)
print(ballena.lugar)
# Utilizar la función del archivo "operaciones" #
print(sumar(12, 78))