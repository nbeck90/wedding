from django import forms


class ResponseForm(forms.Form):

    ACCEPT = 'Joyfully Accept'
    DECLINE = 'Regretfully Decline'

    RESPONSES = (
        (ACCEPT, 'Joyfully Accept'),
        (DECLINE, 'Regretfully Decline')
    )

    name = forms.CharField(max_length=256)
    number = forms.IntegerField()
    email = forms.EmailField()
    response = forms.ChoiceField(choices=RESPONSES)
    comment = forms.CharField(widget=forms.Textarea)
