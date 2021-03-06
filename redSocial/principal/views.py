from principal.models import *
from django_messages.models import Message
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.template import RequestContext
from principal.forms import *
from principal.models import *
from django.utils import timezone
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q #para usar or
import datetime
import math
from django.contrib.auth.models import User


def index(request):
    return render(request, 'users/login.html')

#def index(request):
#	return render(request, 'principal/index.html')

@login_required
def diario(request):
	diarios = EntradaDiario.objects.all()

    	return render(request, 'principal/diario.html',  {'diarios':diarios})

@login_required
def agenda(request):
	agendas = EntradaAgenda.objects.all()

    	return render(request, 'principal/agenda.html',  {'agendas':agendas})

@login_required
def frasecomun(request):
	frasescomun = FraseComun.objects.all()

    	return render(request, 'principal/frasecomun.html',  {'frasescomun':frasescomun})

@login_required
def timeline(request):
	pensamiento = Pensamientos.objects.all().order_by('-fecha')

    	return render(request, 'principal/timelinePensamientos.html',  {'pensamiento':pensamiento})

@login_required
def comentarios(request):
		 
	perfildestino = get_object_or_404(Perfil,usuario=request.user, esActivo=True)
	comentario = Comentario.objects.filter(esChat=False).order_by('-fecha')
	print perfildestino
	list = Comentario.objects.filter(perfilDestino=perfildestino, esChat=False, esPrivado=True, estaLeido=False)
	print list
	for comentPriv in list: 
		print comentPriv
		comentPriv2=Comentario.objects.get(pk=comentPriv.id)
		print comentPriv2
		#form = ComentarioLeidoForm(request.POST.get('estaLeido'), request.FILES, instance=comentPriv)
		#print form
		#form.estaLeido=True
		#print form
		comentPriv2.estaLeido=True
		comentPriv2.save()

		mensaje = Message()#perfilDestino=user Poner destinatario.
		mensaje.subject="Comentario privado al perfil " + comentPriv.perfilDestino.alias + " ha sido leido"		
		mensaje.body="Comentario privado al perfil " + comentPriv.perfilDestino.alias + " enviado desde tu perfil " + comentPriv.perfilOrigen.alias + " ha sido leido. Texto del mensaje: " + comentPriv2.texto
		

		try:
			administrador = User.objects.get(username="admin")#perfil
			mensaje.sender=administrador
			print administrador
			print request.user
		except ObjectDoesNotExist, e:
			mensaje.sender=request.user

		mensaje.recipient=comentPriv.perfilOrigen.usuario
		mensaje.sent_at=datetime.datetime.now()
		mensaje.save()	

		
		print True

		#form.save()
		print "guardado"

	lista=[]
    	for i in comentario:
	
		if i.esPrivado == False:
			x1=i.perfilOrigen.usuario.coordx
			y1=i.perfilOrigen.usuario.coordy
			x2=perfildestino.usuario.coordx
			y2=perfildestino.usuario.coordy
			try:
				distancia=111.302 * math.sqrt(((x2 - x1) **2) + ((y1 - y2) **2))
				if distancia<=1.3:
					print distancia
					print "esta cerca"
					lista.append(i)
			#lat=y long=x
			except ObjectDoesNotExist, e:
				pass
		else:
			lista.append(i)


			
			
			#print math.sqrt(((x2 - x1) **2) + ((y1 - y2) **2))

	#context={'perfil':dato, 'form':form}


    	return render(request, 'principal/timelineComentarios.html',  {'comentario':lista})



###########  DIARIO ########################
@login_required
def diario_detalle(request, diario_id): 

	diario = get_object_or_404(EntradaDiario, pk=diario_id) # Para acceder a la clave primaria

	return render(request, 'principal/diario_detalle.html',
		                     {'diario':diario})

@login_required
def diario_crear(request):

	if request.method == 'POST':
		form = DiarioForm(request.POST,request.FILES)
		if form.is_valid():
			submission = form.save(commit=False)
			#user = User.objects.get(id=request.user.id)
			submission.autor = UsuarioRegistrado.objects.get(id=request.user.id)
			submission.save()
			form.save()

			#print request.post['id_imagen']
			return redirect('diarios')
	else:
		form = DiarioForm()

	return render(request, 'principal/diario_crear.html',
		                      {'form':form},
		                      context_instance=RequestContext(request))
@login_required
def diario_editar(request, diario_id):
	diario = get_object_or_404(EntradaDiario, pk=diario_id)
	if request.method == 'POST':
		form = DiarioForm(request.POST, request.FILES, instance=diario)
		if form.is_valid():
			form.save()
			return redirect('diarios')
	else:
		form = DiarioForm(instance=diario)
	return render(request, 'principal/diario_editar.html', 
							  {'form': form},
							  context_instance=RequestContext(request))
@login_required
def diario_borrar(request, diario_id):
	diario = get_object_or_404(EntradaDiario, pk = diario_id)
	diario.delete()
    	return redirect('diarios')

##################### AGENDA #################################
@login_required
def agenda_detalle(request, agenda_id): 

	agenda = get_object_or_404(EntradaAgenda, pk=agenda_id) # Para acceder a la clave primaria

	return render(request, 'principal/agenda_detalle.html',
		                     {'agenda':agenda})
@login_required
def agenda_crear(request):

	if request.method == 'POST':
		form = AgendaForm(request.POST)
		if form.is_valid():
			submission = form.save(commit=False)
			#user = User.objects.get(id=request.user.id)
			submission.autor = UsuarioRegistrado.objects.get(id=request.user.id)
			submission.save()
			form.save()
			return redirect('agendas')
	else:
		form = AgendaForm()

	return render(request, 'principal/agenda_crear.html',
		                      {'form':form},
		                      context_instance=RequestContext(request))
@login_required
def agenda_editar(request, agenda_id):
	agenda = get_object_or_404(EntradaAgenda, pk=agenda_id)
	if request.method == 'POST':
		form = AgendaForm(request.POST, request.FILES, instance=agenda)
		if form.is_valid():
			form.save()
			return redirect('agendas')
	else:
		form = AgendaForm(instance=agenda)
	return render(request, 'principal/agenda_editar.html',
							  {'form': form},
							  context_instance=RequestContext(request))
@login_required
def agenda_borrar(request, agenda_id):
	agenda = get_object_or_404(EntradaAgenda, pk = agenda_id)
	agenda.delete()
    	return redirect('agendas')

##################### FRASECOMUN ################################# 	
@login_required
def frasecomun_detalle(request, frasecomun_id): 

	frasecomun = get_object_or_404(FraseComun, pk=frasecomun_id) # Para acceder a la clave primaria

	return render(request, 'principal/frasecomun_detalle.html',
		                     {'frasecomun':frasecomun})
@login_required
def frasecomun_crear(request):
	if (request.user.is_superuser and request.user.is_staff):
		if request.method == 'POST':
			form = FraseComunFormAdmin(request.POST)
			if form.is_valid():
				submission = form.save(commit=False)
				#user = User.objects.get(id=request.user.id)
				submission.esGeneral = True
				submission.save()
				form.save()
				return redirect('frasescomun')
		else:
			form = FraseComunFormAdmin()
	else:
		if request.method == 'POST':
			form = FraseComunForm(request.POST)
			if form.is_valid():
				submission = form.save(commit=False)
				#user = User.objects.get(id=request.user.id)
				submission.autor = Perfil.objects.get(usuario=request.user, esActivo=True)
				submission.save()
				form.save()
				return redirect('frasescomun')
		else:
			form = FraseComunForm()

	return render(request, 'principal/frasecomun_crear.html',
		                      {'form':form},
		                      context_instance=RequestContext(request))
@login_required
def frasecomun_editar(request, frasecomun_id):
	frasecomun = get_object_or_404(FraseComun, pk=frasecomun_id)
	if (request.user.is_superuser and request.user.is_staff):
		if request.method == 'POST':
			form = FraseComunFormAdmin(request.POST, request.FILES, instance=frasecomun)
			if form.is_valid():
				form.save()
				return redirect('frasescomun')
		else:
			form = FraseComunFormAdmin(instance=frasecomun)

	else:
		if request.method == 'POST':
			form = FraseComunForm(request.POST, request.FILES, instance=frasecomun)
			if form.is_valid():
				form.save()
				return redirect('frasescomun')
		else:
			form = FraseComunForm(instance=frasecomun)
	return render(request, 'principal/frasecomun_editar.html',
							  {'form': form},
							  context_instance=RequestContext(request))
@login_required
def frasecomun_borrar(request, frasecomun_id):
	frasecomun = get_object_or_404(FraseComun, pk = frasecomun_id)
	frasecomun.delete()
    	return redirect('frasescomun')
##################### PENSAMIENTOS ################################# 
@login_required
def pensamiento_crear(request):

	if request.method == 'POST':
		form = PensamientoForm(request.POST)
		if form.is_valid():
			submission = form.save(commit=False)
			#user = User.objects.get(id=request.user.id)
			submission.autor = Perfil.objects.get(usuario=request.user, esActivo=True)
			submission.save()
			form.save()
			return redirect('/timeline')
	else:
		form = PensamientoForm()

	return render(request, 'principal/pensamiento_crear.html',
		                      {'form':form},
		                      context_instance=RequestContext(request))

@login_required #este esta sin implementar
def pensamiento_borrar(request, pensamiento_id):
	pensamiento = get_object_or_404(Pensamientos, pk = pensamiento_id)
	pensamiento.delete()
    	return redirect('/timeline')

##################### COMENTARIOS #################################
@login_required
def comentario_crear(request):
	frasescomun = FraseComun.objects.all()
	if request.method == 'POST':
		form = ComentarioForm(request.POST)
		if form.is_valid():
			submission = form.save(commit=False)
			#user = User.objects.get(id=request.user.id)
			submission.perfilOrigen  = Perfil.objects.get(usuario=request.user, esActivo=True)
			submission.save()
			form.save()
			return redirect('/comentarios')
	else:
		form = ComentarioForm()

	return render(request, 'principal/comentario_crear.html',
		                      {'form':form,'frasescomun':frasescomun },
		                      context_instance=RequestContext(request))

@login_required
def comentario_priv_crear(request,perfil_id):
	frasescomun = FraseComun.objects.all()
	if request.method == 'POST':
		form = ComentarioForm(request.POST)
		if form.is_valid():
			submission = form.save(commit=False)
			#user = User.objects.get(id=request.user.id)
			submission.perfilOrigen  = Perfil.objects.get(usuario=request.user, esActivo=True)
    			submission.perfilDestino  = Perfil.objects.get(pk=perfil_id, esActivo=True)
			submission.esPrivado = True
			submission.save()
			form.save()
			return redirect('/comentarios')
	else:
		form = ComentarioForm()

	return render(request, 'principal/comentario_crear.html',
		                      {'form':form,'frasescomun':frasescomun },
		                      context_instance=RequestContext(request))

@login_required 
def comentario_borrar(request, comentario_id):
	comentario = get_object_or_404(Comentario, pk = comentario_id)
	comentario.delete()
    	return redirect('/comentarios')


@login_required 
def comentario_ocultar(request, comentario_id):
	comentario = get_object_or_404(Comentario, pk = comentario_id)
	comentario.estaOculto=True
	comentario.save()

	historial=HistComentariosVisib(comentario=comentario, visible=False)
	historial.save()

    	return redirect('/comentarios')

@login_required 
def comentario_mostrar(request, comentario_id):
	comentario = get_object_or_404(Comentario, pk = comentario_id)
	comentario.estaOculto=False
	comentario.save()

	historial=HistComentariosVisib(comentario=comentario, visible=True)
	historial.save()

    	return redirect('/comentarios')

##################### CERCANOS #################################

@login_required(login_url='/users/login')
def cercanos(request):
    list = Perfil.objects.filter(esActivo=True).order_by('alias')
    context = {'cercanos': list}
    return render(request, 'cercanos.html', context)

#---------------------Perfiles---------------------------


@login_required
def misperfiles(request):
	usuario=UsuarioRegistrado.objects.get(username=request.user.username)

	pVerdadero = Perfil.objects.filter(usuario=usuario.id,esVerdadero=True)#perfil verdadero

 
	pFalso =Perfil.objects.filter(usuario=usuario.id,esVerdadero=False)#perfil falso
	
#pFalso =0#= Perfil.objects.get(usuario=usuario.id,esVerdadero=False)#perfil falso
	try:
		pVerdadero = Perfil.objects.get(usuario=usuario.id,esVerdadero=True)#perfil verdadero
		v=1
	except ObjectDoesNotExist, e:
		pVerdadero=0
		v=0
	#raise Exception({pVerdadero})
	try:
		pFalso = Perfil.objects.get(usuario=usuario.id,esVerdadero=False)#perfil verdadero
		f=1
	except ObjectDoesNotExist, e:
		pFalso=0
		f=0

	context={'pVerdadero':pVerdadero, 'pFalso':pFalso, 'v':v, 'f':f}


	return render(request,'misperfiles.html',context)



#nuevoPerfil
def nuevop(request,v):
	if request.method== 'POST':
		form=perfilForm(request.POST,request.FILES)
		if form.is_valid():			
			form = form.save(commit=False)
			usuario=UsuarioRegistrado.objects.get(username=request.user.username)
			#raise Exception({usuario.id})
			form.usuario = usuario	

			try:
				verifica = Perfil.objects.get(usuario=usuario.id, esActivo=True)#perfil
				v3=1
			except ObjectDoesNotExist, e:
				v3=0
			#raise Exception({v3})
			print v
			if int(v) == 1:
				form.esVerdadero=True
				print "verdadero"
			else:
				form.esVerdadero=False
				print "falso"
			if v3==0:
				form.esActivo=True
				request.session['fotografia'] = form.fotografia
				print "no habia activo"
			form.save()
			
			#user2_id=ublog
			return redirect('/perfiles/misperfiles')
	else:
		form=perfilForm()
	context={'form':form}
	return render(request,'nuevop.html',context)

#editarPerfil
@login_required
def editp(request,v,perfil_id):
	#raise Exception({v})
	perfil=get_object_or_404(Perfil,pk=perfil_id)
	if request.method== 'POST':
		form=perfilForm(request.POST,request.FILES, instance=perfil)
		if form.is_valid():
			if v==1:
				form.esVerdadero=True
			else:
				form.esVerdadero=False

			if perfil.esActivo==True:
				request.session['fotografia']= request.POST['fotografia']
				#request.session['fotografia'] = form.Fotografia
			form.save()
			return redirect('/perfiles/misperfiles')
	else:
		form=perfilForm(instance=perfil)
	context={'form':form}
	return render(request,'nuevop.html',context)

@login_required
def detalle_perfil(request, perfil_id):
    dato = get_object_or_404(Perfil, pk=perfil_id)
    #if request.method == 'POST':

    form = PerfilVisitado(request.POST.get('perfil'), request.FILES)

    print form
#		if form.is_valid():
    #submission = form.save()
    user = User.objects.get(id=request.user.id)
    form.perfilOrigen  = Perfil.objects.get(usuario=request.user, esActivo=True)
 
    form.perfilDestino  = Perfil.objects.get(pk=perfil_id)#perfil
    #perfil distinto
    
    if int(form.perfilOrigen.id) == int(perfil_id):
	print form.perfilOrigen.id
	print perfil_id
	print "entra"#pass
    else:
	form.save()



		#perfil origen y destino el mismo
    #form.perfilDestino  = Perfil.objects.get(pk=perfil_id, esActivo=True)

    #submission.save()

    caracteristicas = TipoVotacion.objects.all()
			#return redirect('/archivos')
    #else:
    #form = PerfilVisitado(request.POST, request.FILES)

    mediavotos = MediaVotos.objects.filter(perfilMedia=perfil_id)
    miperfil=Perfil.objects.get(usuario=request.user, esActivo=True)

    votacion = Votacion.objects.filter(perfilOrigen=miperfil,perfilDestino=perfil_id)

    context={'perfil':dato, 'caracteristicas':caracteristicas, 'votacion':votacion, 'mediavotos':mediavotos,'miperfil':miperfil}
    return render(request,'perfil.html',context)

@login_required
def votar(request, perfil_id,caract_id,valorVoto):#falta enviar la notificacion, lo del anonimo
	
	miperfil=Perfil.objects.get(usuario=request.user, esActivo=True)

	pdestino=Perfil.objects.get(pk=perfil_id)

	tipov=TipoVotacion.objects.get(pk=caract_id)


	try:
		verifica = Votacion.objects.get(perfilDestino=pdestino, perfilOrigen=miperfil, tipoVotacion = tipov)#perfil
		print "Ya has votado"
	except ObjectDoesNotExist, e:
 		
		votos=Votacion.objects.filter(perfilDestino=pdestino)
		print miperfil
		form = Votacion(perfilOrigen=miperfil,puntuacion=valorVoto) 

		if miperfil.votoAnonimo == True:
			form.esAnonima=True
		else:
			form.esAnonima=False

			mensaje = Message()#perfilDestino=user Poner destinatario.
			mensaje.subject=miperfil.alias + " te ha puntuado en " + tipov.nombre

			mensaje.body=miperfil.alias + " te ha puntuado en " + tipov.nombre + " con una puntuacion de " + valorVoto


			try:
				administrador = User.objects.get(username="admin")#perfil
				mensaje.sender=administrador
				print administrador
				print request.user
			except ObjectDoesNotExist, e:
				mensaje.sender=request.user
			
			mensaje.recipient=pdestino.usuario
			mensaje.sent_at=datetime.datetime.now()
			mensaje.save()	


		form.tipoVotacion = tipov
		form.perfilDestino  = pdestino
		print form.tipoVotacion
		form.save()

		votos=Votacion.objects.filter(perfilDestino=pdestino, tipoVotacion = tipov)
		media=0
		contador=0
		for v in votos:
			media=media+v.puntuacion	
			contador=contador+1
		media=int(media/contador)

		try:
			mediav = MediaVotos.objects.get(perfilMedia=pdestino, tipoVotacion = tipov)#perfil

			votos=Votacion.objects.filter(perfilDestino=pdestino, tipoVotacion = tipov)
			media=0
			contador=0
			for v in votos:
				media=media+v.puntuacion	
				contador=contador+1
			media=int(media/contador)
			
			mediav.valorMedia=media
			#print "Ya has votado"
		except ObjectDoesNotExist, e:	
	
			mediav=MediaVotos(valorMedia=valorVoto,tipoVotacion=tipov,perfilMedia=pdestino)
			#raise Exception({mediav.tipoVotacion})
		mediav.save()
	return redirect('/perfiles/verPerfil/%d'%int(perfil_id));


#seleccionarp
@login_required
def seleccionarp(request):
	#raise Exception({group1})
	if request.method== 'POST':
		usuario=UsuarioRegistrado.objects.get(username=request.user.username)
		variable=request.POST.get('group1', '')
		
		try:
			pv = Perfil.objects.get(usuario=usuario.id,esVerdadero=True)
			v1=1
		except ObjectDoesNotExist, e:
			v1=0

		
		try:
			pf = Perfil.objects.get(usuario=usuario.id,esVerdadero=False)
			v2=1
		except ObjectDoesNotExist, e:
			v2=0

		if v1 == 1 and v2 == 1:
			if variable=='1':
				pv.esActivo=True
				request.session['fotografia'] = pv.fotografia
				pf.esActivo=False
		
			elif variable=='2':
				pv.esActivo=False
				pf.esActivo=True
				request.session['fotografia'] = pf.fotografia
			pv.save()
			pf.save()
		return redirect('/perfiles/misperfiles')

	context={}
	return render(request,'misperfiles.html',context)

##################### CARACTERISTICAS #################################

@login_required
def caract(request):
	comentario = TipoVotacion.objects.all()

    	return render(request, 'principal/caract.html',  {'comentario':comentario})

@login_required
def caract_crear(request):

	if request.method == 'POST':
		form = CaractForm(request.POST)
		if form.is_valid():
			#submission = form.save(commit=False)
			#user = User.objects.get(id=request.user.id)
			#submission.perfilOrigen  = Perfil.objects.get(usuario=request.user)
			#submission.save()
			form.save()
			return redirect('/caracteristicas')
	else:
		form = CaractForm()

	return render(request, 'principal/caract_crear.html',
		                      {'form':form},)

@login_required 
def caract_borrar(request, caract_id):
	caract = get_object_or_404(TipoVotacion, pk = caract_id)
	caract.delete()
    	return redirect('/caracteristicas')

@login_required
def caract_editar(request,caract_id):
	#raise Exception({v})
	caract=get_object_or_404(TipoVotacion, pk = caract_id)
	if request.method== 'POST':
		form=CaractForm(request.POST,request.FILES, instance=caract)
		if form.is_valid():
			form.save()
			return redirect('/caracteristicas')
	else:
		form=CaractForm(instance=caract)
	context={'form':form}
	return render(request,'principal/caract_crear.html',context)



from filetransfers.api import *

@login_required
def download(request, fichero_id):

    # get the object by id or raise a 404 error
    object = get_object_or_404(Fichero, pk=fichero_id)
    print object.url
    return serve_file(request, object.url,save_as=True)

@login_required
def upload(request,perfil_id):

	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			submission = form.save(commit=False)
			user = User.objects.get(id=request.user.id)
			submission.perfilOrigen  = Perfil.objects.get(usuario=request.user, esActivo=True)

			submission.perfilDestino  = Perfil.objects.get(pk=perfil_id, esActivo=True)
			submission.save()
			form.save()
			return redirect('/archivos')
	else:
		form = UploadForm(request.POST, request.FILES)

	return render(request, 'principal/upload.html',
		                      {'form':form},)
 
@login_required
def archivos(request):
	archivo = Fichero.objects.all()

    	return render(request, 'principal/archivos.html',  {'archivo':archivo})

#			submission.autor = Perfil.objects.get(usuario=request.user, esActivo=True)
@login_required
def historial(request):
	Propietario = Perfil.objects.get(usuario=request.user, esActivo=True)
    	list = Comentario.objects.filter(Q(perfilOrigen=Propietario,esChat=True) | Q(perfilDestino=Propietario,esChat=True))

	lista_nueva = []
	lista_nueva2 = []
 	for i in list:
		
		
		if int(i.perfilOrigen.id) != int(Propietario.id):
			lista_nueva2.append([i.perfilOrigen.id, i.perfilOrigen.alias])

		if int(i.perfilDestino.id) != int(Propietario.id):
			lista_nueva2.append([i.perfilDestino.id, i.perfilDestino.alias])
	for j in lista_nueva2:

		if j not in lista_nueva:
			lista_nueva.append(j)

    	return render(request, 'principal/historialChats.html',  {'perfilesunicos':lista_nueva})

def forgotPassword(request):

	if request.method == 'POST':
		form = PassPerdido(request.POST,instance=UsuarioRegistrado)
		if True:
			#submission = form.save(commit=False)
			#user = User.objects.get(id=request.user.id)
			#submission.perfilOrigen  = Perfil.objects.get(usuario=request.user, esActivo=True)
			#submission.perfilDestino  = Perfil.objects.get(pk=perfil_id, esActivo=True)
			#submission.save()
			#form.save()
			print form
			user = UsuarioRegistrado.objects.get(email=email)
			return redirect('users/login.html"')
	else:
		form = PassPerdido()

	return render(request, 'principal/recuperarContrasena.html',
		                      {'form':form},context_instance=RequestContext(request))





