def userRegister(db):
    print("REGISTRO DE USUARIO:")
    user = input("Ingrese su nuevo usuario: ")
    password = int(input("Ingrese su nueva contraseña: "))
    db[user] = password
    return user, password

def getDB(db):
    print("ACCEDIENDO A LA BASE DE DATOS:")
    for key, value in db.items():
        print(f"El user es: --{key}-- y la contraseña es: --{value}--\n")