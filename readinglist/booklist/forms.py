from django import forms

class AddBook(forms.Form):
  title = forms.CharField(required=True)
  author = forms.CharField(required=True)