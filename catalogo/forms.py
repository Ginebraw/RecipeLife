from django import forms
from django.db.models.fields import files
from django.forms import ModelForm, fields
from .models import Receta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecetaForm(ModelForm):

    class Meta:
        model = Receta
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
