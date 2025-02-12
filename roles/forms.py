from django import forms
from .models import Role
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name', 'description']

class SignupForm(UserCreationForm):  
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  