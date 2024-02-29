from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def create_course(request):
    if request.method == "POST": #Cuando apreto el btn submit
        newCourse = Course(name=request.POST["name"], comision=request.POST["comision"])
        #Leer la data y guardarla en la DB
        newCourse.save()
        return render(request, "index.html")
    
    return render(request, "courses.html")

def create_delivered(request):
    if request.method == "POST":
        infoForm = DeliveredForm(request.POST) #Almacena la info que se puso en el form
        if infoForm.is_valid():
            infoDic = infoForm.cleaned_data #Convierte la info del form en un diccionario
            newDelivered = Deliverable(
                name=infoDic["name"], 
                deadline=infoDic["deadline"], 
                delivered=infoDic["delivered"]
            )
            newDelivered.save()
            return render(request, "index.html")
    else:
        infoForm = DeliveredForm()

    return render(request, "delivered.html", {"form": infoForm})

def see_course(request):
    if request.GET: #Solo si es que hay una busqueda
        name =  request.GET["name"] #Leer el diccionario de info del formulario y obtengo el valor de busqueda
        #courses = Course.objects.filter(name__icontains=name) #Filtrar todos los cursos que contengan el caractere/s que se ingreso
        courses = Course.objects.filter(name__iexact=name) #Filtrar todos los cursos que contengan el mismo name que se ingreso
        message = f"Estamos buscando al curso {name}..."
        return render(request, "seeCourses.html", {"courses": courses, "message": message})
    
    return render(request, "seeCourses.html") #Si todavia no hay una busqueda

def create_student(request):
    student_1 = Students(name="Lionel", lastname="Messi", email="leomessi10@gmail.com", age=35)
    student_2 = Students(name="Cristiano", lastname="Ronaldo", email="crisronaldo7@gmail.com", age=39)
    student_1.save()
    student_2.save()
    info = {"name1": student_1.name, "lastname1": student_1.lastname, "name2": student_2.name, "lastname2": student_2.lastname}

    return render(request, "students.html", info) #1er Arg --- request / 2do Arg --- template / 3er Arg --- context(dic)
