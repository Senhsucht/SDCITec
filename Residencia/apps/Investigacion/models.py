from django.db import models

# Create your models here.

#Modelo de tipo de documento (Ej. Fullpaper, Conference Paper, etc.)
class Tdoc(models.Model):
    tdoc = models.CharField(max_length=25,unique=True)
    descr = models.CharField(max_length=200)
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s"%(self.tdoc,self.descr)

#Modelo de formato del documento (Ej. IEEE, Springer)
class Fdoc(models.Model):
    fdoc = models.CharField(max_length=25,unique=True)
    descr = models.CharField(max_length=200)
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s"%(self.fdoc,self.descr)

#Modelo de topicos para documentos (Ej. Informatica, Medicina, etc.)
class Topicos(models.Model):
    topico = models.CharField(max_length=25,unique=True)
    descr = models.CharField(max_length=200)
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s"%(self.topico,self.descr)

#Modelo de keywords para los documentos
class Keywords(models.Model):
    keyword = models.CharField(max_length=25,unique=True)
    descr = models.CharField(max_length=200)
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s : %s"%(self.keyword,self.descr)

#Modelo de investigaciones
class Investigacion(models.Model):
    titulo = models.CharField(max_length=250)
    lugar = models.CharField(max_length=150)
    fecha = models.DateField()
    abstract = models.CharField(max_length=250)
    id_tdoc = models.ForeignKey('Tdoc')
    id_fdoc = models.ForeignKey('Fdoc')
    id_topico = models.ForeignKey('Topicos')
    id_key = models.ManyToManyField('Keywords')
    docfile = models.FileField(upload_to='documents/%Y/%m/%d/')
    ult_act = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s"%(self.titulo)

# Modelo de historial de investigaciones
class Hist_inv(models.Model):
    id_inv = models.ForeignKey('Investigacion')
    titulo = models.CharField(max_length=250)
    fecha = models.DateField()
    abstract = models.CharField(max_length=250)
    ult_act = models.DateField(auto_now_add=True)


    def __unicode__(self):
        return "%s - %s"%(self.id_inv,self.id_key)
