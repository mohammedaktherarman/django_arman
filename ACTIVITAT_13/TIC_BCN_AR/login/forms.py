from django import forms

class FormulariPersona(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
