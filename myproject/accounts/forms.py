# accounts/forms.py

from django import forms
from .models import User, Organization

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    organization_name = forms.CharField(label="Название вашей организации")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'telegram_id']

    def save(self, commit=True):
        user = super().save(commit=False)
        org = Organization.objects.create(name=self.cleaned_data['organization_name'])
        user.organization = org
        user.is_admin = True
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
