from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def students_home (request):
    students = Articles.objects.order_by('name_student')
    return render(request, 'students/students_home.html', {'students': students})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_home')
        else:
            error = 'Форма неверна'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'students/create.html', data)
