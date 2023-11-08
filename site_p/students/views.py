from django.shortcuts import render
from .models import Articles

def students_home (request):
    students = Articles.objects.order_by('name_student')
    return render(request, 'students/students_home.html', {'students': students})