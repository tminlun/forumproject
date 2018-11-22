from django import forms

#登录
class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=3, max_length=10)
    password = forms.CharField(required=True, min_length=6, max_length=15)

class RegisteredForm(forms.Form):
    username = forms.CharField(required=True, min_length=3, max_length=10)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=15)
    password_again = forms.CharField(required=True, min_length=6, max_length=15)
