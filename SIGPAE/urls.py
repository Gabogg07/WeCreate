from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^cargar/$', views.cargar_archivo, name='cargar'),
	url(r'^transcripcion/$', views.transcripcion, name='transcripcion'),
]