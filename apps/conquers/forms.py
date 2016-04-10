from django import forms
from django.contrib.auth.models import User
from apps.conquers import models

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileForm(forms.ModelForm):

    class Meta:
        model = models.UserProfile
        fields = ('nombre', 'last_name', 'type_user', 'comunity')


class ActivityForm(forms.ModelForm):

    class Meta:
        model = models.Activity
        fields = ('comunity', 'fields')