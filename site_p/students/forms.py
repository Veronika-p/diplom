from .models import Articles
from django.forms import ModelForm, TextInput, NumberInput, DateInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name_student', 'number_class', 'word_class','login1', 'password1']

        widgets = {
            "name_student": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО ученика'
            }),
            "number_class": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер класса'
            }),
            "word_class": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Буква класса'
            }),
            "login1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "password1": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }
