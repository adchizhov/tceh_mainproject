# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from .models import PhoneProduct

__author__ = 'adchizhov'


class PhoneProductForm(forms.ModelForm):
    class Meta:
        model = PhoneProduct
        fields = [
            'sku',
            'manufacturer',
            'phone_model',
            'os_version',
            'chipset',
            'phone_RAM_memory',
            'phone_memory',
            'camera',
            'size_screen',
            'weight',
            'size',
            'description',
            'price',
        ]


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={'invalid': 'Введите пароль в верном виде'},
        label='Пароль',
    )
    email = forms.EmailField(
        widget=forms.TextInput,
        error_messages={'invalid': 'Введите e-mail в верном виде'},
        label="E-mail",
    )
    username = forms.CharField(
        widget=forms.TextInput,
        error_messages={'invalid': 'Введите логин в верном виде'},
        label="Логин",
    )

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    error_messages = {'duplicate_username': 'Пользователь с таким логином уже существует'}

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
            raise forms.ValidationError(
                self.error_messages['duplicate_username'],
                code='duplicate_username',
            )
        except User.DoesNotExist:
            return username