from django.shortcuts import render,get_object_or_404,redirect
# from django.templates import RequestContext
from .forms import AutorForm
from .models import *
from Residencia.apps.Investigacion.models import Fdoc, Tdoc, Topicos, Investigacion
from Residencia.apps.Eventos.models import Part_eve,Evento
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User , Group
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    ctx={'mensaje':' '}

    return render_to_response('General/index.html',ctx)

def logout(request):
    logout(request)


class login(TemplateView):
    template_name = 'General/index.html'


def NuevoUsuario(request):
    ctx={'mensaje':' '}

    if request.POST:
        #Generar nuevo User de Django
        usuario = request.POST.get('usuario')
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        ape_pat = request.POST.get('ape_pat')
        ape_mat = request.POST.get('ape_mat')
        p1 = request.POST.get('contra1')
        p2 = request.POST.get('contra2')

        lname = ape_pat + ape_mat
        if p1 == p2:

            try:
                usr = User.objects.create_user(
                username=usuario,first_name=nombre,last_name=lname,password=p1
                )
                gp = Group.objects.get(name='autor')
                usr.groups.add(gp)

                usr.save()

                #Generar nuevo Usuario de sistema
                a = Usuario()

                a.user = usr
                a.nombre = nombre
                a.ape_pat = ape_pat
                a.ape_mat = ape_mat
                a.edad = request.POST.get('edad')
                a.direccion = request.POST.get('direccion')
                a.tel = request.POST.get('tel')
                a.email = request.POST.get('email')
                a.institucion = request.POST.get('org')
                a.ciudad = request.POST.get('ciudad')
                a.pais = request.POST.get('pais')

                a.save()
                ctx={'mensaje':'Registro exitoso!'}
                return redirect('/',ctx)

            except IntegrityError as e:
                if 'UNIQUE constraint' in e.message:
                    ctx={'mensaje':'Nombre de usuario ocuapado :( '}
                    return render(request,'Autores/AltaUsuario.html',ctx)
        else:
            ctx={'mensaje':'La contrasena no coincide! :( '}
            return render(request,'Autores/AltaUsuario.html',ctx)

    return render(request,'Autores/AltaUsuario.html',ctx)

@login_required(login_url='/')
def ConUsuarios(request):

    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)
    obj = Usuario.objects.all()

    ctx={'mensaje':obj,'uactivo':uactive}

    return render(request,'Autores/ConAutores.html',ctx)

@login_required(login_url='/')
def UserView(request,user,template='Autores/UserView.html'):

    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    profile = get_object_or_404(Usuario,user__username=user)

    uaut = Autores.objects.filter(id_autor=profile)
    upart = Part_eve.objects.filter(id_usr=profile)

    uinv =[];

    for inv in uaut:
        i = get_object_or_404(Investigacion,titulo= inv)
        uinv.append(i)

    ueve  =[];

    for part in upart:
        i = get_object_or_404(Evento,id= part.id_evento.id )
        ueve.append(i)


    uv = get_object_or_404(Usuario,user__username=user)
    return render(request,template, {'uv':uv,'uactivo':uactive,'uinv':uinv,'ueve':ueve})#,context_instance=RequestContext(request))

@login_required(login_url='/')
def UpdateView(request,user,template='Autores/UpdateView.html'):
    # obj = Usuario.objects.all(username=user)

    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    uv = get_object_or_404(Usuario,user__username=user)


    if request.POST:

        if ""!=request.POST.get('nombre'):
            uv.nombre = request.POST.get('nombre')

        if ""!=request.POST.get('edad'):
            uv.edad = request.POST.get('edad')

        if ""!=request.POST.get('ape_pat'):
            uv.ape_pat = request.POST.get('ape_pat')

        if ""!=request.POST.get('ape_mat'):
            uv.ape_mat = request.POST.get('ape_mat')

        if ""!=request.POST.get('direc'):
            uv.direccion= request.POST.get('direc')

        if ""!=request.POST.get('tel'):
            uv.tel = request.POST.get('tel')

        if ""!=request.POST.get('email'):
            uv.email = request.POST.get('email')

        if ""!=request.POST.get('inst'):
            uv.institucion = request.POST.get('inst')

        if ""!=request.POST.get('ciudad'):
            uv.ciudad = request.POST.get('ciudad')

        if ""!=request.POST.get('pais'):
            uv.pais = request.POST.get('pais')

        if ""!=request.POST.get('filebutton'):
            uv.imagen = request.FILES['filebutton']

        uv.save()

        return redirect('/perfil/%s/' % user)

    return render(request,template, {'uv':uv,'uactivo':uactive})#,context_instance=RequestContext(request))

@login_required(login_url='/')
def Dashboard(request):

    u = request.user.get_username()

    tdoc = Tdoc.objects.all()
    fdoc = Fdoc.objects.all()
    topic = Topicos.objects.all()

    uactive = get_object_or_404(Usuario,user__username=u)
    ctx = {'uactivo':uactive}

    return render(request,'General/dashboard.html',ctx)
