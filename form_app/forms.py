from django import forms
from django.core import validators  #Django's inbuilt validators!



def check_for_z(input_str):
    if input_str[0].lower() != 'z':
        raise forms.ValidationError('Name Needs to Start With Z')

class MyFirstForm(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    #required=False means no need to be filled by user HiddenInput means it will be in background HTML but won't be shown on the page
    botcatcher = forms.CharField(required=False,
                                    widget=forms.HiddenInput,
                                    validators=[validators.MaxLengthValidator(0)])

                                #that validators.MaxLengthValidator(0) does same job as below <3





#   MY OWN VALIDATOR!!!!!!!!!!!!!!!!!!!
#these validator functions which raise an error should have their names NECESSARILY start with 'clean_'
#    def clean_botcatcher(self):
#        botcatcher = self.cleaned_data['botcatcher']
#        if len(botcatcher):
#            raise forms.ValidationError("GOTCHA BOT SMD!")


#        return botcatcher
