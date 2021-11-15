# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import Nurse
# from apps.users.models import CustomUser
# from apps.users.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )


class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm Password", "class": "form-control"}
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Phone Number", "class": "form-control"}
        )
    )
    document = forms.FileField(
        widget=forms.ClearableFileInput(),
        label="Document",
        help_text="Maximum file size: 200MB",
        max_length=200,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "document",
        )
    
    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
