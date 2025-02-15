from django import forms
from .models import Login

class FormulariPersona(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

# Amb el ModelForm per alguna cosa em dona error, no em verifica les dades per saber si existeix el usuari esta en la base de dades sino que intenta inserta el que es posa al formulari

# class FormulariPersona(forms.ModelForm):
#     class Meta:
#         model = Login
#         fields = '__all__'


