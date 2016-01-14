from django.db import models


ACCEPT = 'Joyfully Accept'
DECLINE = 'Regretfully Decline'

RESPONSE_CHOICES = (
    (ACCEPT, 'Joyfully Accept'),
    (DECLINE, 'Regretfully Decline')
)


class RSVP(models.Model):
    name = models.CharField(max_length=25, default="Your Name", null=True)
    number = models.TextField(default="Your number", null=True)

    email = models.CharField(max_length=45, default="Your email", null=True)

    response = models.CharField(choices=RESPONSE_CHOICES,
                                max_length=25,
                                null=True)

    comment = models.TextField(null=True)
