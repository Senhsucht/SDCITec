from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    url(r'^altapaper/',NuevoPaper,name='NuevoPaper'),
    url(r'^conpaper/',ConPaper,name='ConPaper'),
    url(r'^paper/(?P<paper>.*)/$',InterPaper,name='InterPaper'),
    )
