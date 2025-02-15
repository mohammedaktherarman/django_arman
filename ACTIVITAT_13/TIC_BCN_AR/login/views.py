from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import FormulariPersona
from .models import Login


# Vistes de Login sense Session:

# def inici(request):
#     return render(request, 'inici.html')

# def formulari(request):
#     if request.method == 'POST':
#         form = FormulariPersona(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
            
#             try:
#                 user = Login.objects.get(email=email)
#                 if user.password == password:  
                 
#                     return redirect('inici')  
#                 else:
#                     messages.error(request, 'credencials errònies')
                    
#             except Login.DoesNotExist:
#                 messages.error(request, 'credencials errònies')

#     else:
#         form = FormulariPersona()

#     return render(request, 'form.html', {'form': form})

# Vistes de Login amb Session:

def inici(request):
    if 'user_id' not in request.session:
        return redirect('formulari')

    return render(request, 'inici.html')

def formulari(request):
    if 'user_id' in request.session:  
        return redirect('inici')

    error_message = ""
    form = FormulariPersona()

    if request.method == 'POST':
        form = FormulariPersona(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Login.objects.filter(email=email).first()
        if user:
            if user.password == password:  
                request.session['user_id'] = user.id  
                return redirect('inici')
            else:
                error_message = 'Credencials errònies'
        else:
            error_message = 'Credencials errònies'

    return render(request, 'form.html', {'form': form, 'error_message': error_message})

def logout(request):
    request.session.flush() 
    return redirect('formulari')  
