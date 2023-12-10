from django.db import models
import random
import string




class Articles(models.Model):

    def gen_rand_login(length):
        characters = string.ascii_letters + string.digits
        login = ''.join(random.choice(characters) for _ in range(length))
        return login

    def gen_rand_password(length):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    name_student = models.CharField('ФИО', max_length=100)
    number_class = models.IntegerField('Номер класса')
    word_class = models.CharField("Буква класса", max_length=10)
    login1 = models.CharField("Логин", max_length=8, default=gen_rand_login(8))
    password1 = models.CharField("Пароль", max_length=8, default=gen_rand_password(8))


    def __str__(self):
        return self.name_student
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

class Tasks(models.Model):
    number_tasks = models.IntegerField('Номер в ЕГЭ')
    image_tasks = models.ImageField('Картинка')
    otvet_tasks = models.CharField('Правильный отет', max_length=100)

    def __str__(self):
        return self.number_tasks
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'