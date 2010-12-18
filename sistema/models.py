from django.db import models
from django.contrib import admin
#from django.contrib.auth.models import User


#class usuario(models.Model):
#  nombre = models.CharField(max_length=15)
#  clave = models.CharField(max_length=10)
#  def __str__(self):
#        return self.nombre
class congregacion(models.Model):
   id_cong = models.AutoField(max_length=5,primary_key=True,blank=True)
   nombre_cong = models.CharField(max_length=30,verbose_name=u'Nombre congregacion',help_text=u'Ingrese nombre congregacion.')
   direccion_cong = models.CharField(max_length=30,verbose_name='Direccion')
   COM_CHOICE = ((u'Concepcion',u'Concepcion'),(u'Talcahuano',u'Talcahuano'),(u'Chiguayante',u'Chiguayante'),
		  (u'Coronel',u'Coronel'))
   comuna_cong = models.CharField(max_length=30,verbose_name='Comuna',choices = COM_CHOICE)
   ciudad_cong = models.CharField(max_length=30,verbose_name='Ciudad')
   fecha_inicio_cong = models.DateField(verbose_name='Fecha Inicio')
   fecha_fin_cong = models.DateField(verbose_name='Fecha Fin')
   VIG_CHOICES = ((u'V',u'Vigente'),
                  (u'N',u'No Vigente'))  
   vigencia = models.CharField(max_length=1,choices = VIG_CHOICES)
   def __unicode__(self):
       return self.nombre_cong

class Publicador(models.Model):
   id_pub = models.AutoField(max_length=5,primary_key=True,blank=True)
   nombrep_pub = models.CharField(max_length=20)
   nombres_pub = models.CharField(max_length=20)
   apellidop_pub = models.CharField(max_length=20)
   apellidom_pub = models.CharField(max_length=20)
   
   	 



#   class Admin:
#       list_display = ('nombre_cong', 'direccion_cong', 'comuna_cong')
#       ordering = ('nombre_cong')
#       search_fields = ('nombre_cong')

#class congregacionAdmin(admin.ModelAdmin):
#    list_display = ('nombre_cong', 'direccion_cong')
# 
# Create your models here.
