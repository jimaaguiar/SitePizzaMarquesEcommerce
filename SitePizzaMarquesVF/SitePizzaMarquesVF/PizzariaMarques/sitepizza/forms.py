from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Perfil

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username..."}),label="Username")
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Email..."}), label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Introduza password..."}), label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirme password..."}), label="Password")
    class Meta:
        model = User
        fields = ['username', 'email',]

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = False
        self.fields['email'].label = False
        self.fields['password1'].label = False
        self.fields['password2'].label = False

class PerfilForm(ModelForm):
    morada = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Ex: Rua da Rosa nº2 1ºEsq."}), label="morada")
    telemovel = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Telemóvel..."}), label="telemovel")
    class Meta:
        model = Perfil
        fields = ['morada', 'telemovel',]

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        self.fields['morada'].label = False
        self.fields['telemovel'].label = False