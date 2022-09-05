from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
        ]
        widgets = {
            'password': forms.PasswordInput,
            'email': forms.EmailInput
        }

class ConnectForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)