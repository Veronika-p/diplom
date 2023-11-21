from django.urls import path
from  . import views

urlpatterns = [
    path('', views.students_home, name='students_home'),
    path('create', views.create, name='create')
]