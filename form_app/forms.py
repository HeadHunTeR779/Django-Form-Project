from django import forms
from django.core import validators  #Django's inbuilt validators!



class MyFirstForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    re_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


    def clean(self):     # just clean so its for validation of all the fields in the form <3
        all_cleaned_data = super().clean()
        email = all_cleaned_data['email']
        re_email = all_cleaned_data['re_email']

        if email != re_email:
            raise forms.ValidationError("Make Sure Mails Match.")




#   MY OWN VALIDATOR!!!!!!!!!!!!!!!!!!!
#these validator functions which raise an error should have their names NECESSARILY start with 'clean_'
#    def clean_botcatcher(self):
#        botcatcher = self.cleaned_data['botcatcher']
#        if len(botcatcher):
#            raise forms.ValidationError("GOTCHA BOT SMD!")


#        return botcatcher
