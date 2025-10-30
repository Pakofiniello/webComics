from django import forms 

class register_form(forms.Form):
    username = forms.CharField(max_length=20, label="Nome utente")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)
    check_password = forms.CharField(label = " Conferma la Password", widget = forms.PasswordInput)
    email = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label="Nome utente")
    password = forms.CharField(label = "Password", widget = forms.PasswordInput)


