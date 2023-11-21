from .models import Articles
from django.forms import ModelForm, TextInput, NumberInput, DateInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name_student', 'date_student', 'age_student', 'number_class']

        widgets = {
            "name_student": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО ученика'
            }),
            "date_student": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения'
            }),
            "age_student": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "number_class": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер класса'
            })
        }
