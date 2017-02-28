from django.db import models
from Residencia.apps.Investigacion.models import *
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.

#Modelo de usuario en el sistema
class Usuario(models.Model):
    user = models.OneToOneField(User, unique=True)
    nombre = models.CharField(max_length=30)
    ape_pat = models.CharField(max_length=30)
    ape_mat = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    direccion  = models.CharField(max_length=200)
    tel = models.PositiveIntegerField()
    email = models.CharField(max_length=50)
    institucion = models.CharField(max_length=150)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='PerfilUSR/',default='PerfilUSR/default.jpg')
    # id_tusr = models.ForeignKey('Tusr')
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s, %s"%(self.user,self.ape_pat,self.nombre)

#Modelo de relacion de autores respecto a investigaciones
class Autores(models.Model):
    id_autor = models.ManyToManyField(Usuario)
    id_inv = models.OneToOneField('Investigacion.Investigacion')
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s"%(self.id_inv)
