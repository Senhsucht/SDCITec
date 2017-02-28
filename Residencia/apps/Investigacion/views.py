from django.shortcuts import render,get_object_or_404,redirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from .models import *
from Residencia.apps.Autores.models import Autores, Usuario
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

@login_required(login_url='/')
def NuevoPaper(request):
    tdoc = Tdoc.objects.all()
    fdoc = Fdoc.objects.all()
    topic = Topicos.objects.all()

    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    ctx={'mensaje':'Registre su paper','tdoc':tdoc,'fdoc':fdoc,'topic':topic,'uactivo':uactive}

    if request.POST:

        # nkey = request.POST.get('keyword')
        titulo = request.POST.get('titulo')
        lugar = request.POST.get('lugar')
        fecha = request.POST.get('fecha')
        abstract = request.POST.get('abstract')

        tdoc = request.POST.get('tdoc')
        fdoc = request.POST.get('fdoc')
        top = request.POST.get('topico')

        keylist = request.POST.get('listkeywords')

        if titulo or lugar or fecha or abstract != "" :

                td = Tdoc.objects.get(id=tdoc)
                fd = Fdoc.objects.get(id=fdoc)
                top = Topicos.objects.get(id=top)

                i = Investigacion()

                i.titulo = titulo
                i.lugar = lugar
                i.fecha = fecha
                i.abstract = abstract
                i.id_tdoc = td
                i.id_fdoc = fd
                i.id_topico = top
                i.docfile = request.FILES['filebutton']

                i.save()

                inv = get_object_or_404(Investigacion,titulo=titulo)

                a = Autores()
                a.id_inv=inv

                a.save()

                a.id_autor.add(uactive)

                if len(keylist) > 0:
                    kl = keylist.split(",")

                    for key in kl:
                        try:
                            exist = Keywords.objects.get(keyword=key)
                            print exist
                        except ObjectDoesNotExist:
                            k = Keywords()
                            k.keyword = key
                            k.descr = key

                            k.save()

                            exist = Keywords.objects.get(keyword=key)
                            print exit

                        i.id_key.add(exist)
                        print i.id_key




        tdoc = Tdoc.objects.all()
        fdoc = Fdoc.objects.all()
        topic = Topicos.objects.all()
        u = request.user.get_username()
        uactive = get_object_or_404(Usuario,user__username=u)

        ctx={'mensaje': 'Paper registrado!','tdoc':tdoc,'fdoc':fdoc,'topic':topic,'uactivo':uactive}

    # else:
    #     ctx={'mensaje': 'Error en los datos.','tdoc':tdoc,'fdoc':fdoc,'topic':topic}

    return render(request,'Investigacion/AltaPaper.html',ctx)

@login_required(login_url='/')
def ConPaper(request):
    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    obj = Investigacion.objects.all()
    ctx={'mensaje':obj,'uactivo':uactive}

    return render(request,'Investigacion/ConPaper.html',ctx)

@login_required(login_url='/')
def AltaKeyword(request):

    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    ctx={'mensaje':'Registre nueva keyword','uactivo':uactive}

    if request.POST:
        k = Keywords

        k.keyword = request.POST.get('keyword')
        k.descr = request.POST.get('keyword')

        k.save()

        ctx={'mensaje':'Keyword registrada','uactivo':uactive}

    return render(request,'Investigacion/AltaPaper.html',ctx)

@login_required(login_url='/')
def InterPaper(request,paper):
    u = request.user.get_username()
    uactive = get_object_or_404(Usuario,user__username=u)

    p = get_object_or_404(Investigacion,id=paper)
    a = get_object_or_404(Autores,id_inv=p)

    return render(request,'Investigacion/InterPaper.html',{'p':p,'a':a,'uactivo':uactive})
