from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='bank'),
    path('credit/', credit, name='credit'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logoutUser, name='logout'),
    path('account/', account, name='account'),
    path('score/', score, name='score'),
    path('credit/loan/', credit1, name='credit1'),
    path('credit/post/<str:post_id>/', show_post, name='show_post'),


]
