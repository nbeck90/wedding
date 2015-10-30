from django import forms

CHOICES = (('1', 'Joyfully Accept',), ('2', 'Regretfully Decline',))


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_number = forms.CharField(label='Your number', max_length=20)
    your_email = forms.EmailField()
    rsvp = forms.MultipleChoiceField(required=True,
                                     label="RSVP",
                                     widget=forms.RadioSelect,
                                     choices=CHOICES)
