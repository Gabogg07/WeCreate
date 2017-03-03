from django.conf.urls import url

from . import views

urlpatterns = [
<<<<<<< HEAD
	url(r'^$', views.home, name='home'),
	url(r'^$', views.index, name='index'),
	url(r'^cargar/$', views.cargar_archivo, name='cargar'),
	url(r'^transcripcion/$', views.transcripcion, name='transcripcion'),
	url(r'^consulta/$', views.consulta, name='consulta'),
=======
	url(r'^$', views.index, name='index'),
	url(r'^cargar/$', views.cargar_archivo, name='cargar'),
	url(r'^transcripcion/$', views.transcripcion, name='transcripcion'),
>>>>>>> 139fc268705670d855abefb57ba379aecc65dedc
]