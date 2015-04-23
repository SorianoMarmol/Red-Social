#encoding: utf-8

from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from principal.models import *




class MyUserForm(UserCreationForm):
    """A form for creating new users. Includes all the required fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput)

    class Meta:
        model = UsuarioRegistrado
        fields = ('first_name', 'last_name', 'username', 'email', 'fechaNacimiento', 'genero', 'ciudad' , 'direccion', 'coordx', 'coordy','aceptaCondicionesUso')
	hidden = ('coordx', 'coordy')      



    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UsuarioRegistrado.objects.get(username = username)
        except UsuarioRegistrado.DoesNotExist:
            return username
        raise forms.ValidationError("Ya existe un usuario con este nombre.")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1", "")
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError("Las dos contrasenias no coinciden.")
        return password2

    def save(self, commit=True):
        UsuarioRegistrado = super(UserCreationForm, self).save(commit=False)
        UsuarioRegistrado.set_password(self.cleaned_data["password1"])
        UsuarioRegistrado.is_staff = False
        UsuarioRegistrado.is_superuser = False
        if commit:
            UsuarioRegistrado.save()
        return UsuarioRegistrado

    def __init__(self, *args, **kwargs): #cambiar el nombre a los campos en la presentacion
		super(MyUserForm,self).__init__(*args,**kwargs)
		self.fields['first_name'].label="Nombre"
		self.fields['username'].label="Nombre de usuario"
		self.fields['email'].label="Email"
		self.fields['aceptaCondicionesUso'].label="¿Acepta las condiciones de uso?"
		self.fields['email'].required=True
		self.fields['coordx'].widget.attrs['readonly'] = True
		self.fields['coordy'].widget.attrs['readonly'] = True

class editUserGeolocationForm(forms.ModelForm):
    class Meta:
        model = UsuarioRegistrado
	widgets = {'coordx': forms.HiddenInput(),'coordy':forms.HiddenInput() }
        fields = ('coordx', 'coordy')
