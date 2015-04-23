from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'RedSocial.views.home', name='home'),
    #url(r'^RedSocial/', include('RedSocial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    url(r'^users/', include("users.urls")),

    url(r'^diarios/$','principal.views.diario', name='diarios'),
    url(r'^agendas/$','principal.views.agenda', name='agendas'),
    url(r'^frasescomun/$','principal.views.frasecomun', name='frasescomun'),

    url(r'^diarios/(?P<diario_id>\d+)/$','principal.views.diario_detalle',
        name='diario_detalle'),
    
    url(r'^diarios/crear/$','principal.views.diario_crear',
        name='diario_crear'),
    
    url(r'^diarios/editar/(?P<diario_id>\d+)/$','principal.views.diario_editar',
        name='diario_editar'),

    url(r'^diarios/borrar/(?P<diario_id>\d+)/$','principal.views.diario_borrar',
        name='diario_borrar'),

    url(r'^agendas/(?P<agenda_id>\d+)/$','principal.views.agenda_detalle',
        name='agenda_detalle'),
    
    url(r'^agendas/crear/$','principal.views.agenda_crear',
        name='agenda_crear'),
    
    url(r'^agendas/editar/(?P<agenda_id>\d+)/$','principal.views.agenda_editar',
        name='agenda_editar'),

    url(r'^agendas/borrar/(?P<agenda_id>\d+)/$','principal.views.agenda_borrar',
        name='agenda_borrar'),

    url(r'^frasescomun/(?P<frasecomun_id>\d+)/$','principal.views.frasecomun_detalle',
        name='frasecomun_detalle'),
    
    url(r'^frasescomun/crear/$','principal.views.frasecomun_crear',
        name='frasecomun_crear'),
    
    url(r'^frasescomun/editar/(?P<frasecomun_id>\d+)/$','principal.views.frasecomun_editar',
        name='frasecomun_editar'),


    url(r'^frasescomun/borrar/(?P<frasecomun_id>\d+)/$','principal.views.frasecomun_borrar',
        name='frasecomun_borrar'),

    url(r'^pensamiento/crear/$','principal.views.pensamiento_crear',
        name='pensamiento_crear'),
    url(r'^timeline/$','principal.views.timeline',
        name='timeline_pensamientos'),
    url(r'^pensamiento/borrar/(?P<pensamiento_id>\d+)/$','principal.views.pensamiento_borrar',
        name='pensamiento_borrar'),

    url(r'^comentario/crear/$','principal.views.comentario_crear',
        name='comentario_crear'),
    url(r'^comentarioPriv/crear/(?P<perfil_id>\d+)$','principal.views.comentario_priv_crear',
        name='comentario_privado'),
    url(r'^comentarios/$','principal.views.comentarios',
        name='timeline_comentarios'),
    url(r'^comentario/borrar/(?P<comentario_id>\d+)/$','principal.views.comentario_borrar',
        name='comentario_borrar'),
    url(r'^comentario/ocultar/(?P<comentario_id>\d+)/$','principal.views.comentario_ocultar',
        name='comentario_ocultar'),
    url(r'^comentario/mostrar/(?P<comentario_id>\d+)/$','principal.views.comentario_mostrar',
        name='comentario_mostrar'),

    url(r'^caracteristicas/crear/$','principal.views.caract_crear'),
    url(r'^caracteristicas/$','principal.views.caract'),
    url(r'^caracteristicas/borrar/(?P<caract_id>\d+)/$','principal.views.caract_borrar'),
    url(r'^caracteristicas/editar/(?P<caract_id>\d+)/$','principal.views.caract_editar'),

    url(r'^cercanos/$','principal.views.cercanos',
        name='vercercanos'),
    url(r'^actualizarLoc/$','users.views.userEditGeo',
        name='actualizarDatosGeoUser'),
	
    url(r'^chat/', include('djangoChat.urls')),
    url(r'^historial/$','principal.views.historial'),

    url(r'^perfiles/misperfiles$', 'principal.views.misperfiles', name='misperfiles'),
    url(r'^perfiles/nuevop/(?P<v>\d+)$', 'principal.views.nuevop', name='nuevop'),
    url(r'^perfiles/editp/(?P<v>\d+)/(?P<perfil_id>\d+)$','principal.views.editp',name='editp'),
    url(r'^perfiles/verPerfil/(?P<perfil_id>\d+)$','principal.views.detalle_perfil'),
    url(r'^perfiles/seleccionarp$','principal.views.seleccionarp',name='seleccionarp'),

    url(r'^passPerdida/$','principal.views.forgotPassword'),
    url(r'^pass/', include('password_reset.urls')),
    url(r'^votar/(?P<perfil_id>\d+)/(?P<caract_id>\d+)/(?P<valorVoto>\d+)$','principal.views.votar'),


    url(r'^upload/(?P<perfil_id>\d+)$','principal.views.upload',name='principal.views.upload'),
    url(r'^download/(?P<fichero_id>\d+)$','principal.views.download',name='principal.views.download'),
    url(r'^archivos/$','principal.views.archivos'),

    url(r'^mensajes/', include('django_messages.urls')),
    url(r'^$', 'django_messages.views.inbox'),

    
    #url(r'^$','users.views.userLogin',),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
