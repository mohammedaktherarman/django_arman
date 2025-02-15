from django.shortcuts import render
from .forms import formulariPersona

def formulari(request):
    form = formulariPersona()
    context = {'form':form}
    return render(request, 'form.html', context)
