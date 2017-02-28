from django.conf.urls import include, url
from django.contrib import admin
from Residencia import settings
from django.conf.urls.static import static
from Residencia.apps.Autores.views import login,logout

urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login',{'template_name' : 'General/index.html'}, name='login'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name' : 'General/index.html'}, name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^login/$', login, name='login1'),



    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('Residencia.apps.Autores.urls')),
    # url(r'^aut/', include('Residencia.apps.Autores.urls')),

    url(r'^', include('Residencia.apps.Eventos.urls')),
    # url(r'^eve/', include('Residencia.apps.Eventos.urls')),

    url(r'^', include('Residencia.apps.Investigacion.urls')),
    # url(r'^inv/', include('Residencia.apps.Investigacion.urls')),

    url(r'media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),

]
