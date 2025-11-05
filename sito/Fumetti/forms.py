from django import forms 
from django.contrib.auth.models import User

class register_form(forms.ModelForm):
    username = forms.CharField(max_length=20, label="Nome utente")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    check_password = forms.CharField(label="Conferma Password", widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="Nome utente")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)


