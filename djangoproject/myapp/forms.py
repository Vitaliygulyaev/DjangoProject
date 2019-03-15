from django import forms
from .models import User


class log_in(forms.Form):
    username = forms.CharField(label=u'Имя пользователя')
    userpassword = forms.CharField(label=u'Пароль', widget=forms.PasswordInput())


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password1 = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'Повторите пароль', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        return self.cleaned_data
