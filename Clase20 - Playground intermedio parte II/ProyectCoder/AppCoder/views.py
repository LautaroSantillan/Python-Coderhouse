from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def create_course(request):
    course_1 = Course(name="Python", comision=50054)
    course_1.save()
    course_2 = Course(name="Python", comision=50550)
    course_2.save()
    info = {"name1": course_1.name, "com1": course_1.comision, "name2": course_2.name, "com2": course_2.comision}
    
    return render(request, "courses.html", info)

def see_course(request):

    return render(request, "seeCourses.html")

def create_student(request):
    student_1 = Students(name="Lionel", lastname="Messi", email="leomessi10@gmail.com", age=35)
    student_2 = Students(name="Cristiano", lastname="Ronaldo", email="crisronaldo7@gmail.com", age=39)
    student_1.save()
    student_2.save()
    info = {"name1": student_1.name, "lastname1": student_1.lastname, "name2": student_2.name, "lastname2": student_2.lastname}

    return render(request, "students.html", info) #1er Arg --- request / 2do Arg --- template / 3er Arg --- context(dic)