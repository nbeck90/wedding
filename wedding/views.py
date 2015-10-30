from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

from .forms import NameForm
from django.core.mail import send_mail, BadHeaderError


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('rsvp.html')

    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


def rsvp(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('home.html')
    else:
        form = NameForm()

    return render(request, 'rsvp.html', {'form': form})


def home_page(request):
    return render(request, 'home.html')

