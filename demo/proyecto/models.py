from django.db import models
from django.contrib.auth.models import User
import datetime
class campo(models.Model):
	lista_campos = (
	('CharField','CHAR'),
	('IntegerField','INT'),
	('BooleanField','BOOLEAN'),
	('BigIntegerField','BIG_INTEGER'),
	('BooleanField','BOOLEAN'),
	
	)
	"""Lista de campos"""
	nombre = models.CharField(blank=True, max_length=100)
	tipo = models.CharField(blank=True, max_length=100,choices=lista_campos)
	longitud = models.FloatField(default=100)
	null = models.BooleanField(default=True)

	
	def __unicode__(self):
		return self.nombre

class tabla(models.Model):
	"""Lista de tablas de una aplicacion"""
	nombre = models.CharField(blank=True, max_length=100)
	campo = models.ManyToManyField(campo)
	def __unicode__(self):
		return self.nombre

class proyecto(models.Model):
	"""Lista de proyectos"""
	user = models.ForeignKey(User)
	nombre = models.CharField(blank=True, max_length=100)
	fecha_creacion = models.DateTimeField(blank=True, default=datetime.datetime.now)
	def __unicode__(self):
		return self.nombre


class configuracion(models.Model):
	"""Lista de configuracion"""
	proyecto = models.ForeignKey(proyecto,unique=True)
	tabla = models.ManyToManyField(tabla)
	tiene_static = models.BooleanField(default=True)
	tiene_media = models.BooleanField(default=True)
	url_static = models.CharField(default="static",blank=True, max_length=100)
	url_media = models.CharField(default="media",blank=True, max_length=100)
	def __unicode__(self):
		return self.proyecto.nombre

