from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request): 
    return render(request, 'front.html', {'name': 'Mosh'})