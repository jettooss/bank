from django.contrib import admin
from .models import *


@admin.register(personal_data1)
class personal_data_admin1(admin.ModelAdmin):
    list_display = \
        ('idd', "passport_series", "passport_number", "habitation", "registration", 'genders', 'first_name',
         'last_name')


@admin.register(card)
class card_admin(admin.ModelAdmin):
    list_display = ( 'card_number', "term", "balance", 'name', 'Cvv')


@admin.register(homes)
class homes_admin(admin.ModelAdmin):
    list_display = ( 'complex', 'description', "link", "metro", 'photo', 'street')


@admin.register(housing_cost)
class housing_admin(admin.ModelAdmin):
    list_display = (
        'complex', 'title', "title1", 'title2', "title3", 'title4', 'area', "area1", 'area2', "area3", 'area4',
        'prices',
        "prices1", 'prices2', "prices3", 'prices4')


@admin.register(credit)
class credit_admin(admin.ModelAdmin):
    list_display = ('pk', 'login', 'loan', 'term', 'percent', 'type_loan', 'datetime')


@admin.register(estate)
class estate_admin(admin.ModelAdmin):
    list_display = ('login', 'name_complex', 'price')


@admin.register(information)
class information_admin(admin.ModelAdmin):
    list_display = ('login', 'relationship', 'children', 'salary')
# @admin.register(mortgage)
# class mortgage_admin(admin.ModelAdmin):
#     list_display = ('pk', 'login', 'loan', 'term', 'percent', 'type_loan', 'datetime','status')