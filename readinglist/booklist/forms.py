from django import forms

class Addbook(forms.Form):
    title = forms.CharField(required=True)
    author = forms.CharField(required=True)

class Adduserbook(forms.Form):
    userid = forms.IntegerField(widget=forms.HiddenInput())
    bookid = forms.IntegerField(widget=forms.HiddenInput())

class Deletebook(forms.Form):
    userfaveid = forms.IntegerField(widget=forms.HiddenInput())
