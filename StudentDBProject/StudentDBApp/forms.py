from django import forms;
from django.core import validators

class StudentLoginForm(forms.Form):
    username=forms.CharField();
    password=forms.CharField(widget=forms.PasswordInput())


class SignupForm(forms.Form):
    name= forms.CharField(label='enter your name:')
    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(label='Reenter Password',widget=forms.PasswordInput)
    email=forms.EmailField()
    def clean(self):
        total_cleaned_data=super().clean()
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['repasword']
        if pwd!=rpwd:
            raise forms.ValidationError('both password must same')