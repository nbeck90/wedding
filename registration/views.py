from django.views.generic import CreateView
from django.shortcuts import render
from django.views.generic.list import ListView
from registration.forms import ResponseForm
from django.http import HttpResponseRedirect

from wedding.models import RSVP


class RSVPList(ListView):
    model = RSVP


def rsvp_list(request):
    reqs = RSVP.objects.orderby('date_created')
    return render(request, 'rsvp_list.html', {'rsvp_list': reqs})


def rsvp(request):
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/list')
    else:
        form = ResponseForm()

    return render(request, 'rsvp.html', {'form': form})


class RSVP(CreateView):
    model = RSVP
    context_object_name = 'rsvp'
    success_url = '/list'
    fields = [
        'name',
        'number',
        'email',
        'response',
        'comment'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RSVP, self).form_valid(form)

    def get_form(self, form_class):
        form = super(RSVP, self).get_form(form_class)
        return form
