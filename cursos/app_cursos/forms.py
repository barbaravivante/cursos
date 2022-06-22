from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Alta_cursos(forms.Form):

    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()

class Alta_alumnos(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    nacimiento = forms.DateField()

class Alta_profesor(forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()
    nacimiento = forms.DateField()        

class UserEditForm(UserCreationForm):
    
    #email = forms.EmailField(label="Modificar email")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password1' , 'password2']
        help_text = {k:"" for k in fields}    

