from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    url(r'^nuevoevento/',NuevoEvento,name='NuevoEvento'),
    url(r'^coneventos/',ConEvento,name='ConEvento'),
    url(r'^eventos/(?P<eve>.*)/$',EvenView,name='EvenView'),


    )
