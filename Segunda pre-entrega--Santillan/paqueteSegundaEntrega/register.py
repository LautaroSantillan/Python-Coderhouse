def register(database):
  print("REGISTRO:")
  user = input("Ingrese un nombre de usuario: ")

  while user in database:
    print("¡El usuario ya existe! Por favor, intente devuelta")
    user = input("Ingrese otro nombre de usuario: ")

  password = input("Ingrese una contraseña: ")
  password2 = input("Ingrese otra vez la contraseña: ")

  while password != password2:
    print("Las contraseñas no coinciden. Inténtelo de nuevo")
    password = input("Ingrese una contraseña: ")
    password2 = input("Ingrese otra vez la contraseña: ")

  database[user] = password
  saveData(database)
  print("Proceso de registro finalizado")

# -------------- #

def getData(database):
  print("BUSCANDO INFORMACIÓN EN LA BASE DE DATOS:")

  if not database:
    print("No hay información en la base de datos...")
  else:
    for user, password in database.items():
      print(f"Nombre de usuario: {user} - Contaseña: {password}")

# -------------- #

import json
def saveData(database):
  try:
    ruta = r"C:\Users\EQUIPO\Desktop\Python-Coder\Segunda pre-entrega--Santillan"
    with open(ruta + r"\database.json", 'w') as file:
      json.dump(database, file, indent=2)
    print("Guardado en la base de datos")
  except Exception as e:
    print(f"Error al guardar en la base de datos: {e}")

# -------------- #

def login(database):
  print("INICIO DE SESIÓN:")
  attempts = 0 # intentos
  maxAttempts = 3

  while attempts < maxAttempts:
    user = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if (user in database) and (database[user] == password):
      return print("Has iniciado sesión correctamente!")
    else:
      print("Usuario o Contraseña incorrectos. Inténtelo de nuevo")
      attempts += 1

  print(f"Has superado el límite de intentos ({attempts}). Pruebe más tarde")