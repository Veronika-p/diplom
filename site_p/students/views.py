from django.shortcuts import render, redirect
from .models import Articles, Tasks
from .forms import ArticlesForm


def students_home(request):
    students = Articles.objects.order_by('name_student')
    return render(request, 'students/students_home.html', {'students': students})
def tasks_home(request):
    tasks = Tasks.objects.order_by('number_tasks')
    return render(request, 'students/tasks_home.html', {'tasks': tasks})


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
