from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('index/', index, name="Home"),
    path('CreateCourses/', create_course),
    path('CreateStudents/', create_student),
    path('SeeCourses/', see_course, name="Course"),
]