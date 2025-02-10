from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def inici(request):
    return render(request, 'inici.html')