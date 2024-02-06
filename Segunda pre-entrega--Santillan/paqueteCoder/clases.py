"""IMPORT"""
from paqueteCoder.register import *

# ----- Definción de Clases ----- # 
class Persona:
    def __init__(self, name, lastname, age):
        self.name = name
        self.__lastname = lastname
        self.age = age
    
    def __str__(self):
        return f"Nombre: {self.name} - Apellido: {self.__lastname} - Edad: {self.age}"
    
    def login(self):
        print(f"La persona {self.name} {self.__lastname} se ha logeado!!")
# -------------- #
class Cliente(Persona):
    def __init__(self, name, lastname, age, email, password, address, city):
        super().__init__(name, lastname, age)
        self.email = email
        self.__password = password
        self.__address = address
        self.city = city
    
    def __str__(self):
        return f"DATOS DEL CLIENTE\nNombre y Apellido: {self.name} {self._Persona__lastname} - Edad: {self.age} - Email: {self.email} - Dirección y Ciudad: {self.__address} - {self.city}"
    
    def login(self):
        print(f"El cliente {self.name} {self._Persona__lastname} se ha logeado!!")
    
    def purchase(self, article, price, market):
        print(f"Compra realizada por el Sr {self._Persona__lastname}:\nArticulo: {article}\tPrecio: ${price}\tTienda: {market}")
        print(f"En los próximos minutos recibiras un comprobante de la compra a {self.email}\n")
        
class Admin(Persona):
    def __init__(self, name, lastname, age, email, password, range, city):
        super().__init__(name, lastname, age)
        self.email = email
        self.__password = password
        self.__range = range # creador - tester
        self.city = city
        
    def __str__(self):
        return f"DATOS DEL ADMINISTRADOR\nNombre y Apellido: {self.name} {self._Persona__lastname} - Edad: {self.age} - Email: {self.email} - Rango: {self.__range} - Ciudad: {self.city}"
        
    def login(self):
        print(f"El {self.__range}: {self.name} {self._Persona__lastname}, se ha logeado!!")
        
    def getRange(self):
        print(f"Este admin tiene el status de: {self.__range}")