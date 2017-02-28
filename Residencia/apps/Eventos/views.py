from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import render
from Residencia.apps.Investigacion.models import *
from Residencia.apps.Autores.models import Usuario
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/')
def EvenView(request):
    obj = Evento.objects.all()

    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    ctx={'mensaje':obj,'uactivo':uactive}

    return render(request,'Eventos/ConEventos.html',ctx)

@login_required(login_url='/')
def ConEvento(request):
    obj = Evento.objects.all()

    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    ctx={'mensaje':obj,'uactivo':uactive}

    return render(request,'Eventos/ConEventos.html',ctx)

@login_required(login_url='/')
def NuevoEvento(request):
    teve = Teve.objects.all()
    topic = Topicos.objects.all()
    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    if request.POST:

        # try:
        nombre = request.POST.get('nombre')
        acronimo = request.POST.get('acronimo')
        descr = request.POST.get('descr')
        website = request.POST.get('website')
        ciudad = request.POST.get('ciudad')
        pais = request.POST.get('pais')
        fecha = request.POST.get('fecha')
        organizador = request.POST.get('organizador')
        organ_contact = request.POST.get('contacto')
        te = request.POST.get('teve')
        top = request.POST.get('topico')

        te = Teve.objects.get(id=te)
        top = Topicos.objects.get(id=top)

        edo = Eve_edo.objects.get(eve_edo='Pendiente')

        e = Evento()

        e.nombre = nombre
        e.acronimo = acronimo
        e.descr = descr
        e.descripcion = descr
        e.website = website
        e.ciudad = ciudad
        e.pais = pais
        e.fecha = fecha
        e.organizador = organizador
        e.organ_contact = organ_contact
        e.id_eve_edo = edo
        e.id_teve = te
        e.id_topico = top

        e.save()

        p = Part_eve()
        p.id_usr = uactive
        p.id_tpart = Tpart.objects.get(tpart='Organizador')
        p.id_evento = e
        p.save()

        # teve = Teve.objects.all()
        # topic = Topicos.objects.all()
        # ctx={'teve':teve,'topico':topic,'uactivo':uactive}

        return redirect('/coneventos/')
        # return render(request,'Eventos/AltaEventos.html',ctx)


        #
        # except Exception as e:
        #     raise




    ctx={'teve':teve,'topico':topic,'uactivo':uactive}

    return render(request,'Eventos/AltaEventos.html',ctx)

@login_required(login_url='/')
def EvenView(request,eve):
    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    e = get_object_or_404(Evento,id=eve)



    return render(request,'Eventos/EveView.html',{'e':e, 'uactivo':uactive})
