from django import forms

class InstagramForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    password = forms.CharField(label='Password')

class SignUpForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    password = forms.CharField(label='Password')
    password = forms.CharField(label='Password Again')
    email = forms.EmailField(label='Email')
