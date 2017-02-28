from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import NuevoUsuario,ConUsuarios,UserView,UpdateView,Dashboard

urlpatterns = patterns('',
    url(r'^registrate/',NuevoUsuario,name='NuevoUsuario'),
    url(r'^conusuario/',ConUsuarios,name='ConUsuarios'),
    url(r'^perfil/(?P<user>.*)/$',UserView,name='UserView'),
    url(r'^edit/(?P<user>.*)/$',UpdateView,name='UpdateView'),
    url(r'^dashboard/$',Dashboard,name='Dashboard'),

    )
