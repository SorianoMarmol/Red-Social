from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json
#from djangoChat.models import Message, ChatUser

from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now as utcnow

from django.contrib.auth.decorators import login_required

from django.db.models import Q #para usar or
from principal.models import Comentario,Perfil, UsuarioRegistrado

#UsuarioRegistrado.objects.get(username=user.username)

@login_required(login_url='/users/login')
def index(request, perfil_id):
	request.session['chatDestino'] = perfil_id
	context = {}#'logged_users':logged_users}
	return render(request, 'djangoChat/index.html', context)





#envio de mensajes
@csrf_exempt
def chat_api(request):
	usuario=UsuarioRegistrado.objects.get(username=request.user.username)
	user2 = Perfil.objects.get(usuario=usuario.id,esActivo=True)
	IDperfilDestino= request.session.get('chatDestino')
	perfilDestinatario=Perfil.objects.get(pk=IDperfilDestino)
	#raise Exception({IDperfilDestino})
	if request.method == 'POST':
		d = json.loads(request.body)
		msg =  d.get('msg')
		

		gravatar = user2.fotografia
		m = Comentario(perfilOrigen=user2, perfilDestino=perfilDestinatario,texto=msg, esChat=True, esPrivado=True, conversacionActiva=True)#perfilDestino=user Poner destinatario.
		m.save()

	
	#por poner
	#coordx= models.FloatField(blank=True,null=True) #modificar en el diagrama
	#coordy= models.FloatField(blank=True,null=True) #aniadir al diagrama

		res = {'id':m.id,'msg':m.texto,'user':m.perfilOrigen.alias,'time':m.fecha.strftime('%I:%M:%S %p').lstrip('0'),'gravatar':gravatar}
		data = json.dumps(res)
		return HttpResponse(data,content_type="application/json")
	

	# get request



#Q(perfilOrigen=user2.id, perfilDestino=user2.id) | Q(perfilOrigen=user2.id, perfilDestino=user2.id),
	r = Comentario.objects.filter(Q(perfilOrigen=user2.id, perfilDestino=perfilDestinatario) | Q(perfilOrigen=perfilDestinatario, perfilDestino=user2.id), esPrivado=True,esChat=True).order_by('-fecha')[:70]
#ponenr bien el perfil destino
	res = []

	#raise Exception({request.user.username})
	for msgs in reversed(r): #res.append ahi abajo es el error
		#raise Exception({msgs.perfilOrigen})
		#userx=Perfil.objects.get(alias=msgs.perfilOrigen) #perfil origen es el alias
		#msgs.perfilOrigen
		#raise Exception({request.user.username})
		res.append({'id':msgs.id,'user':msgs.perfilOrigen.alias,'msg':msgs.texto,'time':msgs.fecha.strftime('%I:%M:%S %p').lstrip('0'),'gravatar':user2.fotografia})#gravatar es temporal, luego se pondra la foto.
		#print msgs.id
	
	data = json.dumps(res)
	
	return HttpResponse(data,content_type="application/json")
	#context = {'res': res}
    #return render(request, 'djangoChat/index.html', context)

#vista de usuarios logueados
def logged_chat_users(request):
	
	#raise Exception({request.user.username})
	usuario=UsuarioRegistrado.objects.get(username=request.user.username)


	IDperfilDestino= request.session.get('chatDestino')
	perfilDestinatario=Perfil.objects.get(pk=IDperfilDestino)
	
	#raise Exception({perfilDestinatario.usuario.id})

	uu = Perfil.objects.filter(Q(usuario=usuario.id) | Q(usuario=perfilDestinatario.usuario.id), esActivo=True)#poner el perfil2 en el segundo.

	d = []
	for i in uu:
		d.append({'username': i.alias,'gravatar':i.fotografia,'id':i.id})
	data = json.dumps(d)
	 
#deberia de cargarse la lista de usuarios.
	return HttpResponse(data,content_type="application/json")


def update_time(request):#quitar
	return HttpResponse('Quien eres?')






