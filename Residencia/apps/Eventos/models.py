from django.db import models
from Residencia.apps.Autores.models import *
from Residencia.apps.Investigacion.models import *


# Create your models here.

#Modelo de estados para eventos
class Eve_edo(models.Model):
    eve_edo = models.CharField(max_length=25,unique=True)
    descr = models.CharField(max_length=200)
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s"%(self.eve_edo,self.descr)

#Modelo de tipos de eventos
class Teve(models.Model):
    teve = models.CharField(max_length=25,unique=True)
    descr = models.CharField(max_length=200)
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s"%(self.teve,self.descr)

#Modelo de registros de eventos
class Evento(models.Model):
    nombre = models.CharField(max_length=250)
    acronimo = models.CharField(max_length=25)
    descr = models.CharField(max_length=200)
    website =  models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha = models.DateField()
    organizador = models.CharField(max_length=100)
    organ_contact = models.CharField(max_length=100)
    id_eve_edo = models.ForeignKey('Eve_edo')
    id_teve = models.ForeignKey('Teve')
    id_topico = models.ForeignKey('Investigacion.Topicos')
    descripcion = models.CharField(max_length=500)
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s"%(self.acronimo,self.nombre)

#Modelo de topicos del evento
# class Eve_topicos(models.Model):
#     id_eve = models.ForeignKey('Evento')
#     id_topico = models.ManyToManyField('Investigacion.Topicos')
#     ult_act = models.DateField(auto_now_add=True)
#
#     def __unicode__(self):
#         return "%s : %s"%(self.id_eve,self.id_topico)

#Modelo de tipos de participantes de eventos
class Tpart(models.Model):
    tpart = models.CharField(max_length=25,unique=True)
    descr = models.CharField(max_length=200)
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s"%(self.tpart,self.descr)

#Modelo de usuarios participantes en eventos
class Part_eve(models.Model):
    id_usr = models.ForeignKey('Autores.Usuario')
    id_evento = models.ForeignKey('Evento')
    id_tpart =  models.ForeignKey('Tpart')
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s"%(self.id_usr,self.id_evento)
