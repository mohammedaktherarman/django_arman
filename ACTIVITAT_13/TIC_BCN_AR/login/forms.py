from django.forms import ModelForm 
from .models import Login

class formulariPersona(ModelForm):
    class Meta:
        model = Login
        fields = '__all__'
