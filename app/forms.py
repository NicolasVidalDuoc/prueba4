from django import forms
from django.forms import fields, widgets
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    image = forms.ImageField(required=False)

    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]