from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    professor = {"name": "Roger", "surname": "Sobrino", "age": "17"}
    return render(request, 'index.html', {'nombre':professor["name"],'surname':professor["surname"],'age':professor["age"]})

