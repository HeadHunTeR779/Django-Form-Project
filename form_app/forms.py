from django import forms

class MyFirstForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                    widget=forms.HiddenInput)

#these validator functions which raise an error should have their names NECESSARILY start with 'clean_'
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']

        if len(botcatcher):
            raise forms.ValidationError("GOTCHA BOT SMD!")


        return botcatcher
