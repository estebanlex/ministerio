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
   nombrep_pub = models.CharField(max_length=20,verbose_name='Primer nombre')
   nombres_pub = models.CharField(max_length=20,verbose_name='Segundo nombre')
   apellidop_pub = models.CharField(max_length=20,verbose_name='Apellido Paterno')
   apellidom_pub = models.CharField(max_length=20,verbose_name='Apellido materno')
   fecha_nacimiento_pub = models.DateField(verbose_name='Fecha nacimiento')
   direccion_pub = models.CharField(max_length=30,verbose_name='direccion')
   telefono_pub = models.IntegerField(max_length=13,verbose_name='Telefono')
   id_cong_pub_fk = models.ForeignKey(congregacion,verbose_name='Congregacion')
   ano_bautismo_pub = models.IntegerField(max_length=4,verbose_name='Ano bautismo')
   tipo_pub = models.CharField(max_length=4,verbose_name='Tipo publicador')
   
   def __unicode__(self):
       return self.nombrep_pub
   
   	 



#   class Admin:
#       list_display = ('nombre_cong', 'direccion_cong', 'comuna_cong')
#       ordering = ('nombre_cong')
#       search_fields = ('nombre_cong')

#class congregacionAdmin(admin.ModelAdmin):
#    list_display = ('nombre_cong', 'direccion_cong')
# 
# Create your models here.
