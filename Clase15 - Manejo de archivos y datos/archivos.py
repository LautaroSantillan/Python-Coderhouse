"""IMPORTS"""
import random 
 # ---- #
x = random.randint(10, 100)
print(x)
# ----- Persistencia de Datos ----- #
f = open("C:/Users/EQUIPO/Desktop/Python-Coder/Clase15 - Manejo de archivos y datos/miArchivo.txt", "a")
f.write(str(x))
f.write("\n")
f.close()