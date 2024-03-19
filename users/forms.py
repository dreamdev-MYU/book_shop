from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password bir xil emas")

        return cleaned_data

    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']

        if password_confirm != password:
            raise forms.ValidationError("password bir xil bolishi kerak")
        
        return password_confirm
    
    def clean_username(self):
        username = self.cleaned_data['username']

        if len(username) < 5 or len(username) > 30:
            raise forms.ValidationError("Username 5 va 30 orasida bolishi kerak")
        return username
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if not isinstance(username, str):
            raise forms.ValidationError('username harflardan iborat bolishini tekshiring')
        if len(username) < 5 or len(username) > 30:
            raise forms.ValidationError('Username 5 va 30 orasida bolsin')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        return password
