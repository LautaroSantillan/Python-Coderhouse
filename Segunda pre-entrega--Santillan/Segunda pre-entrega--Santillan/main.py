"""IMPORTS"""
from paqueteSegundaEntrega.register import *
from paqueteSegundaEntrega.clases import Cliente, Admin

# ---- Funcionamiento de la primera pre-entrega ---- # 
"""database = {}
try:
    with open('database.json') as file:
        database = json.load(file)
except FileNotFoundError:
    pass

while True:
    print("\nMENU:")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Ver información de la base de datos")
    print("4. Salir")

    option = input("Seleccione una opción: ")

    if option == "1":
        register(database)
    elif option == "2":
        login(database)
    elif option == "3":
        getData(database)
    elif option == "4":
        break
    else:
        print("Opción inválida. Inténtelo de nuevo.")"""

# ---- Funcionamiento de la segunda pre-entrega ---- # 
cliente_1 = Cliente("Lautaro", "Santillan", 20, "santillanlautaro03@gmail.com", "9854120", "Hipolito Vieytes", "Buenos Aires")
cliente_2 = Cliente("Nazareno", "Perez", 19, "nazitape12@gmail.com", "291008", "Calle 127", "Villa Gesell")
print(cliente_2)

cliente_1.login()

cliente_2.purchase("PS5", 500, "Sony")
cliente_1.purchase("Laptop TUF Gaming", 355, "Asus")
# -------- # 
admin_1 = Admin("Lautaro", "Santillan", 20, "santillanlautaro03@gmail.com", "9854120", "Creador", "Bs. As")
admin_2 = Admin("Tester", "Python", 00, "testerPY@gmail.com", "782135", "Tester", "Bs. As")

print(admin_2)

admin_2.login()
admin_1.getRange()