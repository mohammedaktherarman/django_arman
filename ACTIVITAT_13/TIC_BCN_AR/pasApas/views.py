from django.shortcuts import render

def guardar_sesion(request):
    request.session['usuario'] = 'Arman'
    return render(request, 'guardar_sesion.html')
