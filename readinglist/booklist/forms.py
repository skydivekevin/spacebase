from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class Addbook(forms.Form):
    title = forms.CharField(required=True)
    author = forms.CharField(required=True)

class Adduserbook(forms.Form):
    userid = forms.IntegerField(widget=forms.HiddenInput())
    bookid = forms.IntegerField(widget=forms.HiddenInput())

class Deletebook(forms.Form):
    userfaveid = forms.IntegerField(widget=forms.HiddenInput())

class UserCreationFormEmail(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
