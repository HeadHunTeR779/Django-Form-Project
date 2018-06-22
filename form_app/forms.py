from django import forms

class MyFirstForm(forms.Form):
    name = forms.Charfield()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
