from django.shortcuts import render

def index(request):
    data = {
        'title': 'Веб-приложение для проведения тренировочного ЕГЭ по информатике',
        'values': ['F', 'g','t']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')


