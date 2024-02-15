from django.http import HttpResponse
from datetime import datetime

def saludo(request, nombre):
    
    return HttpResponse(f"Bienvenidos {nombre} a mi página!")

def about(request):
    
    return HttpResponse("Esta página fue creada en clase")

def tiempo(request):
    now = datetime.now() #Usamos el modulo datetime de python
    
    return HttpResponse(f"La hora actual es: {now.hour}:{now.minute}:{now.second}")