"""wedding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$', 'wedding.views.home_page', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rsvp/', 'registration.views.rsvp', name='rsvp'),
    url(r'^rsvp/list', 'registration.views.rsvp_list', name='rsvp_list'),
]

urlpatterns += staticfiles_urlpatterns()
