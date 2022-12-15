from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginUserForm (forms.ModelForm):
    password1 = forms.CharField(max_length=16, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'label': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password1']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }

class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'label': 'Password'}))
    password2 = forms.CharField(max_length=16, label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs= {
              'class': 'form-control'  
            }),
            'email': forms.TextInput(attrs= {
              'class': 'form-control'  
            })
        }


