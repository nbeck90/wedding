from django import forms


class ResponseForm(forms.Form):

    ACCEPT = 'Joyfully Accept'
    DECLINE = 'Regretfully Decline'

    RESPONSES = (
        (ACCEPT, 'Joyfully Accept'),
        (DECLINE, 'Regretfully Decline')
    )

    name = forms.CharField(max_length=256)
    number = forms.CharField()
    email = forms.EmailField()
    response = forms.ChoiceField(choices=RESPONSES)
    comments = forms.CharField(widget=forms.Textarea)
