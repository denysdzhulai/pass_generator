from django.shortcuts import render
import random
import datetime

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    yr = datetime.datetime.now()
    return render(request, 'generator/about.html', {'year': yr.year})

def password(request):
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    symbols = request.GET.get('symbols')

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if(uppercase):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if(numbers):
        characters.extend('1234567890')
    if(symbols):
        characters.extend('!@#$%^&*()_+-?><')

    thepass = ''
    for i in range(length):
        thepass += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepass})