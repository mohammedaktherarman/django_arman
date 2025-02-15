from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import FormulariPersona
from .models import Login

def inici(request):
    return render(request, 'inici.html')

def formulari(request):
    if request.method == 'POST':
        form = FormulariPersona(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                user = Login.objects.get(email=email)
                if user.password == password:  
                 
                    return redirect('inici')  
                else:
                    messages.error(request, 'credencials errònies')
                    
            except Login.DoesNotExist:
                messages.error(request, 'credencials errònies')

    else:
        form = FormulariPersona()

    return render(request, 'form.html', {'form': form})
