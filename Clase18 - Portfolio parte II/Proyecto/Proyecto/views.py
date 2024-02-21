from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
import random 

def index(request):
    now = datetime.now()
    names = {"Lautaro", "Nazareno", "Luciano"} 
    randomNumber = random.randint(0, 10) 
    info = {"names": names, "time": now, "random": randomNumber}
    
    file = open(r"C:\Users\EQUIPO\Desktop\Python-Coder\Clase18 - Portfolio parte II\Proyecto\Proyecto\templates\index.html")
    #Pasar el HTML a algo que Python pueda comprenderlo mejor
    template = Template(file.read())
    file.close()
    
    context = Context(info)
    
    document = template.render(context)
    
    return HttpResponse(document)

def time(request):
    now = datetime.now() #Usamos el modulo datetime de python
    hour = now.hour
    minute = now.minute
    second = now.second
    
    file = open(r"C:\Users\EQUIPO\Desktop\Python-Coder\Clase18 - Portfolio parte II\Proyecto\Proyecto\templates\time.html")
    #Pasar el HTML a algo que Python pueda comprenderlo mejor
    template = Template(file.read())
    file.close()
    
    info = {"hour": hour, "minute": minute, "second": second}
    
    context = Context(info)
    
    document = template.render(context)
    
    return HttpResponse(document)
    
def about(request):
    randomNumber = random.randint(0, 10) 
    
    file = open(r"C:\Users\EQUIPO\Desktop\Python-Coder\Clase18 - Portfolio parte II\Proyecto\Proyecto\templates\about.html")
    #Pasar el HTML a algo que Python pueda comprenderlo mejor
    template = Template(file.read())
    file.close()
    
    info = {"random": randomNumber}
    
    context = Context(info)
    
    document = template.render(context)
    
    return HttpResponse(document)