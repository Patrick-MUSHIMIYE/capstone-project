from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError  

class CustomUserCreationForm(UserCreationForm):  
    first_name = forms.CharField(min_length=5, max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': _('First Name')}))
    second_name = forms.CharField(min_length=5, max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': _('Second Name')}))
    username = forms.CharField(min_length=5, max_length=150, widget=forms.TextInput(attrs={'placeholder': _('Username')})) 
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': _('Email')}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))  
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': _('Confirm Password')})) 
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username = username)
        if new.count():
            raise ValidationError(" User Already Exist")  
        return username  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2 
  
    def save(self, commit = True):  
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['second_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user