from django import forms
from .models import User, Organization

class RegisterForm(forms.ModelForm):
    create_new_org = forms.BooleanField(required=False, label='Создать новую организацию')
    organization_name = forms.CharField(required=False, label='Название организации')

    class Meta:
        model = User
        fields = ['username', 'password', 'telegram_id']

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['create_new_org']:
            org = Organization.objects.create(name=self.cleaned_data['organization_name'])
            user.organization = org
            user.is_admin = True
        if commit:
            user.set_password(self.cleaned_data['password'])
            user.save()
        return user