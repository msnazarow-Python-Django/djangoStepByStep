from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', aboutUs, name='aboutUs'),
    path('contacts/', contacts, name='contacts'),
    path('news/<int:year>', year, name='year'),
    path('signup/', register, name='register'),
    path('addUser/', addUser, name='addUser'),
    path('modelform/', modelform, name='modelform'),
    path('addModalForm/', addModalForm, name='addModalForm')
]
