from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.RequestListView.as_view(
        template_name="requests/requestspage.html",
    ),
        name='requests_page'),
    url(r'^newrequest',
        'registration.views.RSVP',
        name='rsvp',
        ),
]
