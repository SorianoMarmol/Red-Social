from django.conf.urls import patterns, include, url

from djangoChat import views

urlpatterns = patterns('',
    url(r'^(?P<perfil_id>\d+)$', views.index, name='index'),
    #url(r'^$', views.chat_api, name='index'),
    #url(r'^login/$',views.login,name='login'),
    #url(r'^logout/$',views.logout,name='logout'),

    url(r'^api/$',views.chat_api,name='chat_api'),
    url(r'^api/users/$',views.logged_chat_users,name='logged_chat_users'),
    url(r'^api/users/update/$',views.update_time,name='update_time'),
#url(r'^list$', views.userList, name='list'),
)
