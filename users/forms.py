from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='请输入有效的电子邮件地址')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
