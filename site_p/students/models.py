from django.db import models

class Articles(models.Model):
    name_student = models.CharField('ФИО', max_length=100)
    date_student = models.DateField('Дата рождения')
    age_student = models.IntegerField('Возраст')
    number_class = models.IntegerField('Номер класса')

    def __str__(self):
        return self.name_student
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
