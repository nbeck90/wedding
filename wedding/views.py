from django.shortcuts import render
from registration.views import RSVP
from django.views.generic import CreateView


def home_page(request):
    return render(request, 'home.html')


class RSVP(CreateView):
    model = RSVP
    context_object_name = 'rsvp'
    success_url = '/list'
    fields = [
        'name',
        'number',
        'email',
        'response',
        'comments'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RSVP, self).form_valid(form)

    def get_form(self, form_class):
        form = super(RSVP, self).get_form(form_class)
        return form
