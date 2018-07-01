from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Account


class AccountCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('account_id', 'account_type', 'email', 'name')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValueError("Password don't match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user


class AccountChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('account_id', 'password', 'account_type', 'email', 'name', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']
