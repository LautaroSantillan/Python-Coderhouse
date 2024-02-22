from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('index/', index),
    path('CreateCourses/', create_course),
    path('CreateStudents/', create_student),
]