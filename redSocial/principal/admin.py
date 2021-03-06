from django.contrib import admin
from principal.models import *

class UsuarioRegistradoAdmin(admin.ModelAdmin):
   list_display = ('username','first_name', 'last_name', 'email','conectado', 'fechaNacimiento', 'genero', 'ciudad') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('username')
   list_editable = ('first_name', 'last_name', 'email','conectado', 'fechaNacimiento', 'genero', 'ciudad') #para mostrar mas datos sin entrar en su ficha
   list_filter= ('conectado', 'genero', 'ciudad') #barra lateral de filtrado
   list_per_page = 10
   search_fields = ('username','first_name', 'last_name', 'email','conectado', 'fechaNacimiento', 'genero', 'ciudad') #barra de busqueda
   date_hierarchy = 'last_login' #ordenacion

admin.site.register(UsuarioRegistrado,UsuarioRegistradoAdmin)

class PerfilAdmin(admin.ModelAdmin):
   list_display = ('id','alias','usuario','esVerdadero', 'esActivo', 'edad','genero', 'permiteVotar', 'ciudad') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('username')
   list_editable = ('alias','esVerdadero', 'esActivo', 'edad','genero', 'permiteVotar', 'ciudad') #para mostrar mas datos sin entrar en su ficha
   list_filter= ('esVerdadero', 'esActivo','edad','genero', 'permiteVotar','ciudad') #barra lateral de filtrado
   list_per_page = 10
   search_fields = ('usuario','alias','esVerdadero', 'esActivo', 'edad','genero', 'permiteVotar', 'ciudad') #barra de busqueda
   #date_hierarchy = 'last_login'

admin.site.register(Perfil,PerfilAdmin)

class EntradaDiarioAdmin(admin.ModelAdmin):
   list_display = ('id','titulo','autor','fecha', 'lugar') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('username')
   list_editable = ('titulo', 'lugar') #para mostrar mas datos sin entrar en su ficha
   list_filter= ('autor','titulo','fecha', 'lugar') #barra lateral de filtrado
   list_per_page = 10
   search_fields = ('autor','titulo','fecha', 'lugar') #barra de busqueda
   date_hierarchy = 'fecha'  #ordenacion

admin.site.register(EntradaDiario,EntradaDiarioAdmin)

class EntradaAgendaAdmin(admin.ModelAdmin):
   list_display = ('id','titulo','autor','fecha', 'lugar') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('username')
   list_editable = ('titulo', 'lugar') #para mostrar mas datos sin entrar en su ficha
   list_filter= ('autor','titulo','fecha', 'lugar') #barra lateral de filtrado
   list_per_page = 10
   search_fields = ('autor','titulo','fecha', 'lugar') #barra de busqueda
   date_hierarchy = 'fecha'  #ordenacion

admin.site.register(EntradaAgenda,EntradaAgendaAdmin)

class PerfilVisitadoAdmin(admin.ModelAdmin):
   list_display = ('id','perfilOrigen','perfilDestino', 'fecha') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('id','perfilOrigen','perfilDestino')
   #raw_id_fields = ('perfilOrigen','perfilDestino')
   list_filter = ['perfilOrigen', 'perfilDestino','fecha'] #barra lateral de filtrado
   list_per_page = 10
   search_fields = ['perfilOrigen', 'perfilDestino','fecha'] #busqueda por datos
   date_hierarchy = 'fecha'  #ordenacion

admin.site.register(PerfilVisitado, PerfilVisitadoAdmin)

class PensamientosAdmin(admin.ModelAdmin):
   list_display = ('id','autor','tipoPensamiento','publicacion','fecha') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('username')
   list_editable = ('tipoPensamiento','publicacion') #para mostrar mas datos sin entrar en su ficha
   list_filter= ('tipoPensamiento','publicacion','fecha')  #barra lateral de filtrado
   list_per_page = 10
   search_fields = ('tipoPensamiento','publicacion','fecha')  #barra de busqueda
   date_hierarchy = 'fecha'  #ordenacion

admin.site.register(Pensamientos,PensamientosAdmin)

class FicheroAdmin(admin.ModelAdmin):
   list_display = ('nombreFichero','perfilOrigen','perfilDestino','url','fecha') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('username')
   list_editable = ('perfilOrigen','perfilDestino','url') #para mostrar mas datos sin entrar en su ficha
   list_filter= ('perfilOrigen','perfilDestino','fecha') #barra lateral de filtrado
   list_per_page = 10
   search_fields = ('nombreFichero','perfilOrigen','perfilDestino','url','fecha')  #barra de busqueda
   date_hierarchy = 'fecha'  #ordenacion

admin.site.register(Fichero,FicheroAdmin)

admin.site.register(TipoVotacion)

class VotacionAdmin(admin.ModelAdmin):
   list_display = ('id','tipoVotacion','esAnonima','perfilOrigen','perfilDestino','puntuacion') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('username')
   list_editable = ('tipoVotacion','esAnonima') #para mostrar mas datos sin entrar en su ficha
   list_filter= ('tipoVotacion','esAnonima','perfilOrigen','perfilDestino') #barra lateral de filtrado
   list_per_page = 10
   search_fields = ('tipoVotacion','perfilOrigen','perfilDestino')  #barra de busqueda
   #date_hierarchy = 'fecha'  #ordenacion

admin.site.register(Votacion,VotacionAdmin)

admin.site.register(MediaVotos)

class FraseComunAdmin(admin.ModelAdmin):
   list_display = ('id','texto','autor','esGeneral') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('username')
   list_editable = ('texto','autor','esGeneral') #para mostrar mas datos sin entrar en su ficha
   list_filter= ('texto','autor','esGeneral') #barra lateral de filtrado
   list_per_page = 10
   search_fields = ('texto','autor','esGeneral')  #barra de busqueda
   #date_hierarchy = 'fecha'  #ordenacion

admin.site.register(FraseComun,FraseComunAdmin)

class ComentarioAdmin(admin.ModelAdmin):
   list_display = ('id','esPrivado','esAnonima','esChat','estaOculto','conversacionActiva','estaLeido','perfilOrigen','perfilDestino','fecha') #para mostrar mas datos sin entrar en su ficha
   #list_display_links = ('username')
   #list_editable = ('tipoVotacion','esAnonima') #para mostrar mas datos sin entrar en su ficha
   list_filter= ('esPrivado','esAnonima','esChat','estaOculto','conversacionActiva','estaLeido','perfilOrigen','perfilDestino','fecha') #barra lateral de filtrado
   list_per_page = 10
   search_fields = ('texto','perfilOrigen','perfilDestino')  #barra de busqueda
   date_hierarchy = 'fecha'  #ordenacion

admin.site.register(Comentario,ComentarioAdmin) 

admin.site.register(HistComentariosVisib)


