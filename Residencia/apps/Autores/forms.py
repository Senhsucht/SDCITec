from django.forms import ModelForm
from .models import *

class AutorForm(ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
