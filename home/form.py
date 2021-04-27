from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget = forms.PasswordInput())
    password1 = forms.CharField(label='retype password', widget = forms.PasswordInput())
    def clean_password1(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password1 = self.cleaned_data['password1']
            if password1 == password and password:
                return password1
        raise forms.ValidationError("Invalid password")
    
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Username has special characters")
        try:
            User.objects.get(username= username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("This username is already exist")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])
