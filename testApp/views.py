import random

from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.

def home(request):
    articles = Article.objects.all()

    context = {
        'name': 'Michael',
        'articles': articles
    }
    return render(request, 'home.html', context)


def aboutUs(request):
    context = {
        'list': ["Python", "Java", "C++"],
        'mynum': random.randint(49, 51)
    }
    return render(request, 'aboutUs.html', context)


def contacts(request):
    obj = New.objects.get(id=1)
    context = {
        'data': obj
    }
    return render(request, 'contacts.html', context)


def year(request, year):
    list = New.objects.filter(pub_date__year=year)
    context = {
        'list': list,
        'year': year
    }
    return render(request, 'year.html', context)


def register(request):
    context = {
        'form': RegistrationForm
    }
    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        my_register = RegistrationData(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone']
        )
        my_register.save()
        messages.add_message(request, messages.SUCCESS, "You have signup successfully")
    return redirect('register')


def modelform(request):
    context = {
        "modelform": RegistrationModal
    }
    return render(request, "modalform.html", context)


def addModalForm(request):
    my_modalform = RegistrationModal(request.POST)

    if my_modalform.is_valid():
        my_modalform.save()

    return redirect('modelform')
