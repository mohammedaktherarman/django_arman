from django.shortcuts import redirect, render

def guardar_sesion(request):
    request.session['usuario'] = 'Arman'
    return render(request, 'guardar_sesion.html')

def recuperar_sesion(request):
    usuario = request.session.get ('usuario', 'invitado')
    return render(request, 'recuperar_sesion.html', {'usuario': usuario})

def eliminar_sesion(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    return redirect('recuperar_sesion')