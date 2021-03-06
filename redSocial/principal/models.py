from django.db import models
from django.contrib.auth.models import User
from django.core.validators import ValidationError
#zonas horarias
from datetime import *
from django.utils import timezone #zonas horarias

from django.contrib.auth.signals import user_logged_in, user_logged_out  
import urllib, hashlib, binascii

class UsuarioRegistrado(User):
	tiposGeneros2=(
	('Hombre','HOMBRE'),
	('Mujer','MUJER'),
	)
	#nombreUsuario: heredado
	#nombre: heredado
	#apellidos:heredado
	#email: heredado
	#contrasenia: heredado
	conectado = models.BooleanField(default=False)
	fechaNacimiento= models.DateField()
	genero =models.CharField(max_length=33,choices=tiposGeneros2)
	aceptaCondicionesUso = models.BooleanField()
	direccion= models.CharField(max_length=250)
	ciudad=models.CharField(max_length=150) #anadir al diagrama
	coordx= models.FloatField(blank=True,null=True) #modificar en el diagrama
	coordy= models.FloatField(blank=True,null=True) #anadir al diagrama

	def __unicode__(self):
		return unicode(self.username)#no se puede devolver un objeto, solo una cadena

	def clean_fields(self,exclude=None):
		if self.aceptaCondicionesUso == False:
			raise ValidationError({'aceptaCondicionesUso': ["Error debe aceptar las condiciones de uso.",]})




class Perfil(models.Model):
	tiposGeneros=(
	('Hombre','HOMBRE'),
	('Mujer','MUJER'),
	)
	tiposOrientacion=(
	('Heterosexual','HETEROSEXUAL'),
	('Bisexual','BISEXUAL'),
	('Homosexual','HOMOSEXUAL'),
	('Indefinido','INDEFINIDO'),
	)
	tiposRelaciones=(
	('BuscandoAmistad','BUSCANDOAMISTAD'),
	('BuscandoPareja','BUSCANDOPAREJA'),
	('Buscando Sexo','BUSCANDO SEXO'),
	('BuscandoConversacion','BUSCANDOCONVERSACION'),
	('Otros','OTROS'),
	)
	tiposReligion=(
	('Ateo','ATEO'),
	('Agnostico','AGNOSTICO'),
	('Cristiano','CRISTIANO'),
	('Musulman','MUSULMAN'),
	('Judio','JUDIO'),
	('Budista','BUDISTA'),
	('Otra','OTRA'),
	)
	tipoEstadoCivil=(
	('Soltero','SOLTERO'),
	('ConPareja','CONPAREJA'),
	('Casado','CASADO'),
	('RelacionAbierta','RELACIONABIERTA'),
	)

	usuario=models.ForeignKey(UsuarioRegistrado)
	esVerdadero = models.BooleanField()
	esActivo = models.BooleanField()
	alias = models.CharField(max_length=30,unique=True)
	edad = models.IntegerField()
	genero =models.CharField(max_length=33,choices=tiposGeneros)
	orientacionSexual=models.CharField(max_length=33,choices=tiposOrientacion)
	profesion = models.CharField(max_length=30,blank=True)
	estudios = models.CharField(max_length=250,blank=True)
	estadoCivil=models.CharField(max_length=33,choices=tipoEstadoCivil)
	relaciones =models.CharField(max_length=33,choices=tiposRelaciones)
	creenciaReligiosa=models.CharField(max_length=33,choices=tiposReligion)
	intereses = models.CharField(max_length=250,blank=True)
	aficiones = models.CharField(max_length=250,blank=True)
	descripcion = models.CharField(max_length=250,blank=True)
	otraInfo = models.CharField(max_length=250,blank=True)
	permiteVotar = models.BooleanField(default=False)
	fotografia = models.CharField(max_length=300,blank=True)#models.ImageField(upload_to='imagen-diario',blank=True,null=True)
	ciudad=models.CharField(max_length=150,blank=True) #anadir al diagrama
	coordx= models.FloatField(blank=True,null=True) #modificar en el diagrama
	coordy= models.FloatField(blank=True,null=True) #anadir al diagrama
	votoAnonimo = models.BooleanField(default=False)
 
	def __unicode__(self):
		return unicode(self.alias)#no se puede devolver un objeto, solo una cadena


class EntradaDiario(models.Model):
	autor=models.ForeignKey(UsuarioRegistrado)
	titulo = models.CharField(max_length=30)  
	texto = models.CharField(max_length=250)
	fecha = models.DateTimeField(auto_now_add=True)
	imagen = models.ImageField(upload_to='imagendiario',blank=True,null=True)
	lugar = models.CharField(max_length=30) 
	coordx= models.FloatField(blank=True,null=True) #modificar en el diagrama
	coordy= models.FloatField(blank=True,null=True) #anadir al diagrama

	def __unicode__(self):
		return unicode(self.titulo)#no se puede devolver un objeto, solo una cadena
	

class EntradaAgenda(models.Model):
	autor=models.ForeignKey(UsuarioRegistrado)
	titulo = models.CharField(max_length=30)  
	descripcion = models.CharField(max_length=250)
	fecha = models.DateTimeField() #incluira hora (esperemos)
	hora = models.CharField(max_length=100)
	lugar = models.CharField(max_length=30) 
	coordx= models.FloatField(blank=True,null=True) #modificar en el diagrama
	coordy= models.FloatField(blank=True,null=True) #anadir al diagrama


	def __unicode__(self):
		return unicode(self.titulo)#no se puede devolver un objeto, solo una cadena
	


class PerfilVisitado(models.Model):
	perfilOrigen = models.ForeignKey(Perfil, related_name='origenVisitado') #seria foreign key a perfil
	perfilDestino = models.ForeignKey(Perfil, related_name='destinoVisitado') #seria foreign key a perfil
	fecha = models.DateTimeField(auto_now_add=True) #incluia hora (esperemos)

class Fichero(models.Model):
	nombreFichero = models.CharField(max_length=30)  
	fecha = models.DateTimeField(auto_now_add=True) #incluira hora (esperemos)
	perfilOrigen = models.ForeignKey(Perfil, related_name='origenFichero') #seria foreign key a perfil
	perfilDestino = models.ForeignKey(Perfil, related_name='destinoFichero')  #seria foreign key a perfil
	coordx= models.FloatField(blank=True,null=True) #modificar en el diagrama
	coordy= models.FloatField(blank=True,null=True) #anadir al diagrama
	url = models.FileField(upload_to='files') #URL del archivo


	def __unicode__(self):
		return unicode(self.nombreFichero)#no se puede devolver un objeto, solo una cadena


	

class Pensamientos(models.Model):
	tiposPensamientos=(
	('Pensamiento','PENSAMIENTO'),
	('Oferta de Servicio','OFERTA DE SERVICIO'),
	('Demanda de Servicio','DEMANDA DE SERVICIO'),
	)
	autor=models.ForeignKey(Perfil)
	tipoPensamiento =models.CharField(max_length=33,choices=tiposPensamientos)
	publicacion = models.CharField(max_length=250)
	fecha = models.DateTimeField(auto_now_add=True)  
	coordx= models.FloatField(blank=True,null=True) #modificar en el diagrama
	coordy= models.FloatField(blank=True,null=True) #anadir al diagrama

	def __unicode__(self):
		return unicode(self.publicacion)#no se puede devolver un objeto, solo una cadena

	

class TipoVotacion(models.Model):
	nombre =models.CharField(max_length=33)
	def __unicode__(self):
		return unicode(self.nombre)#no se puede devolver un objeto, solo una cadena

class Votacion(models.Model):
	tipoVotacion = models.ForeignKey(TipoVotacion)
	esAnonima = models.BooleanField(default=False)
	perfilOrigen = models.ForeignKey(Perfil, related_name='origenVotacion') 
	perfilDestino = models.ForeignKey(Perfil, related_name='destinoVotacion')
	puntuacion = models.IntegerField() #definir luego entre 1 y 10

	def clean_fields(self,exclude=None):
		if self.puntuacion > 10:
			raise ValidationError({'puntuacion': ["Entre 1 y 10!",]})
		if self.puntuacion < 1:
			raise ValidationError({'puntuacion': ["Entre 1 y 10!",]})

class MediaVotos(models.Model):
	valorMedia= models.IntegerField() #aniadir en el diagrama de clases
	perfilMedia= models.ForeignKey(Perfil)   #seria foreign key a perfil (AL QUE PERTENECE LA MEDIA)
	tipoVotacion= models.ForeignKey(TipoVotacion)   #seria foreign key a TipoVotacion
	def __unicode__(self):
		return unicode(self.perfilMedia)

class FraseComun(models.Model):
	esGeneral = models.BooleanField(default=False)
	autor = models.ForeignKey(Perfil,blank=True,null=True)
	texto = models.CharField(max_length=30)  
	def __unicode__(self):
		return unicode(self.texto)#no se puede devolver un objeto, solo una cadena

class Comentario(models.Model):
	esPrivado = models.BooleanField(default=False)
	esAnonima = models.BooleanField(default=False)
	esChat= models.BooleanField(default=False)
	conversacionActiva= models.BooleanField(default=False) #mantener el chat con la distancia
	estaLeido= models.BooleanField(default=False)
	estaOculto= models.BooleanField(default=False)    
	texto = models.CharField(max_length=200)  

	perfilOrigen = models.ForeignKey(Perfil, related_name='origenComentario')
	perfilDestino = models.ForeignKey(Perfil,blank=True,null=True, related_name='destinoComentario') #permitir en blanco por si no es CHAT (comentario publico)

	fecha = models.DateTimeField(auto_now_add=True) #incluia hora (esperemos)
	coordx= models.FloatField(blank=True,null=True) #modificar en el diagrama
	coordy= models.FloatField(blank=True,null=True) #anadir al diagrama

	def __unicode__(self):
		return unicode(self.texto)#no se puede devolver un objeto, solo una cadena

class HistComentariosVisib(models.Model):
	comentario = models.ForeignKey(Comentario)
	visible= models.BooleanField(default=True)
	fecha = models.DateTimeField(auto_now_add=True) 

	def __unicode__(self):
		return unicode(self.comentario)

#class Message(models.Model):
#	user = models.CharField(max_length=200)
#	message = models.TextField(max_length=200)
#	time = models.DateTimeField(auto_now_add=True)   ==>fecha
#	gravatar = models.CharField(max_length=300)
#	def __unicode__(self):
#		return self.user

