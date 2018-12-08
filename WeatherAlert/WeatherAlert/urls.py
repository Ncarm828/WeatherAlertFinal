"""
Definition of urls for WeatherAlert.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin

import app.forms
import app.views

admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^weather/$', app.views.weather, name='weather'),
    url(r'^profile/$', app.views.profile, name='profile'),
    url(r'^signup/$',app.views.user_signup,name='signup'),
    url(r'^verify/$',app.views.verify,name='verify'),
    url(r'^cancel/$',app.views.cancel,name='cancel'),
    url(r'^logout/$', app.views.logout_view,name='logout'),

    url(r'^login/$',app.views.user_login,name='login'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', admin.site.urls),
]
