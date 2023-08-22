from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from .models import *


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={"class": "form-control mb-1"}), label='Имя пользователя')
    email = forms.EmailField(widget=forms.TextInput(
        attrs={"class": "form-control mb-1"}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control mb-1"}),
                                label='Пароль')
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={"class": "form-control mb-1"}),
                                label='Подтвердите пароль')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': "form-control mb-1"}), label='Имя пользователя')
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': "form-control mb-1"}), label='Почта')
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={"class": "form-control mb-1"}), label='Пароль')
    remember_me = forms.BooleanField(required=False, label='Запомнить меня')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control mb-1"}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={"class": "form-control mb-1"}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control mb-1", 'placeholder': 'Аватар'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Расскажите о себе'}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
