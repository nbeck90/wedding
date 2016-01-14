from django.db import models


ACCEPT = 'Joyfully Accept'
DECLINE = 'Regretfully Decline'

RESPONSE_CHOICES = (
    (ACCEPT, 'Joyfully Accept'),
    (DECLINE, 'Regretfully Decline')
)


class RSVP(models.Model):
    name = models.CharField(default="Your Name")
    number = models.CharField(default="Your number")

    email = models.CharField(default="Your email")

    response = models.CharField(max_length=25,
                                choices=RESPONSE_CHOICES,
                                default='Joyully Accept')

    comment = models.CharField(max_length=25,
                               choices=RESPONSE_CHOICES,
                               default='Regretfully Decline')
