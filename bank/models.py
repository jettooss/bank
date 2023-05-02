from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

user = get_user_model()
name = get_user_model()


class personal_data1(models.Model):
    idd = models.OneToOneField(user, on_delete=models.CASCADE, null=True, verbose_name="логин")
    passport_series = models.CharField(max_length=255, verbose_name="серия паспорта")
    passport_number = models.CharField(max_length=255, verbose_name="номер паспорта")
    habitation = models.CharField(max_length=255, verbose_name="проживание в данный  момент")
    first_name = models.CharField(max_length=255, verbose_name="Имя ")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", primary_key=True)
    registration = models.CharField(max_length=255, verbose_name="регистрация")
    Genders = (
        ('a', 'Мужчина'),
        ('b', 'Женщина'),
        ('c', 'Трансформер '),
    )
    genders = models.CharField(choices=Genders, verbose_name="Пол", max_length=1)

    def __str__(self): return str(self.last_name)

    class Meta:
        verbose_name = 'основные данные  людей '
        verbose_name_plural = 'основные данные  людей '


class card(models.Model):
    card_number = models.CharField(max_length=15, verbose_name="номер карты", primary_key=True)
    term = models.CharField(max_length=15, verbose_name="срок действия ")

    balance = models.PositiveBigIntegerField(default=0)
    name = models.OneToOneField(personal_data1, on_delete=models.CASCADE, verbose_name="ФИО")
    Cvv = models.CharField(max_length=3)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'картa'
        verbose_name_plural = 'карты'


class homes(models.Model):
    complex = models.CharField(max_length=255, verbose_name="Название ЖК", primary_key=True)
    link = models.CharField(max_length=255, verbose_name="ссылка ")
    description = models.CharField(max_length=255, verbose_name="описание")
    metro = models.CharField(max_length=255, verbose_name="метро")
    photo = models.CharField(max_length=255, verbose_name="фото")
    street = models.CharField(max_length=255, verbose_name="Улица")

    class Meta:
        verbose_name = 'дома '
        verbose_name_plural = 'дома'


class housing_cost(models.Model):
    complex = models.OneToOneField(homes, on_delete=models.CASCADE, verbose_name="Название дома")
    title = models.CharField(max_length=255, verbose_name="тип квартиры_1")
    title1 = models.CharField(max_length=255, verbose_name="тип квартиры_2")
    title2 = models.CharField(max_length=255, verbose_name="тип квартиры_3")
    title3 = models.CharField(max_length=255, verbose_name="тип квартиры_4")
    title4 = models.CharField(max_length=255, verbose_name="тип квартиры_5")
    area = models.CharField(max_length=255, verbose_name="площадь")
    area1 = models.CharField(max_length=255, verbose_name="площадь")
    area2 = models.CharField(max_length=255, verbose_name="площадь")
    area3 = models.CharField(max_length=255, verbose_name="площадь")
    area4 = models.CharField(max_length=255, verbose_name="площадь")
    prices = models.CharField(max_length=255, verbose_name="цена")
    prices1 = models.CharField(max_length=255, verbose_name="цена")
    prices2 = models.CharField(max_length=255, verbose_name="цена")
    prices3 = models.CharField(max_length=255, verbose_name="цена")
    prices4 = models.CharField(max_length=255, verbose_name="цена")

    class Meta:
        verbose_name_plural = 'Стоимость домов '


class credit(models.Model):
    login = models.ForeignKey(personal_data1, on_delete=models.CASCADE, verbose_name="Логин")
    loan = models.FloatField(verbose_name="Сумма кредита ")
    term = models.FloatField(verbose_name="время ", )
    A = (
        ('О', 'Кредит'),
        ('И', 'Ипотека'),

    )

    type_loan = models.CharField(choices=A, verbose_name="Тип кредита ", max_length=1, default='О')
    percent = models.IntegerField(verbose_name="Проценты ")
    B = (
        ('О', 'Задолжник'),
        ('П', 'в процессе'),
        ('З', 'Завершен'),

    )

    # status = models.CharField(choices=B, verbose_name="статус  кредита ", max_length=1)
    datetime = models.DateTimeField(default=dt.now)

    def get_absolute_url(self):
        return reverse('credit1', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name_plural = 'Кредиты'


class estate(models.Model):
    login = models.ForeignKey(personal_data1, on_delete=models.CASCADE, verbose_name="ФИО", null=True)
    name_complex = models.CharField(verbose_name="Дом ", max_length=255)
    price = models.CharField(verbose_name="стоимость", max_length=255)

    class Meta:
        verbose_name_plural = 'купленные квартиры '


class information(models.Model):
    login = models.OneToOneField(personal_data1, on_delete=models.CASCADE, verbose_name="ФИО")

    c = (
        ('В', 'Взрослые'),
        ('П', 'Подростки'),
        ('Р', 'Ребенок'),
        ('Н', 'Отсутствуют'),

    )
    v = (
        ('В', 'в браке'),
        ('П', 'есть отношения'),
        ('Х', 'Холост'),

    )

    relationship = models.CharField(choices=v, verbose_name="Cемейное положение. ", max_length=1)
    children = models.CharField(choices=c, verbose_name="Есть ли дети ", max_length=1)
    salary = models.IntegerField(verbose_name="ваша средняя зарплата")

    class Meta:
        verbose_name_plural = 'Дополнительная информация людей '

