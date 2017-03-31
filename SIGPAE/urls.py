from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^$', views.index, name='index'),
	url(r'^base/$', views.base, name='base'),
	url(r'^cargar/$', views.cargar_archivo, name='cargar'),
	url(r'^transcripcion/$', views.transcripcion, name='transcripcion'),
	url(r'^consulta/$', views.consulta, name='consulta'),
	url(r'prueba(?P<url>(\w|\W|\s)*)/$',views.prueba,name='prueba')
<<<<<<< HEAD
]   
=======
] 
>>>>>>> wc/Objetivos
