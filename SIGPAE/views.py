from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
import textract
import os
import re

from .models import Document, Historial
from .forms import DocumentForm, ConsultaForm, HistorialForm, MostrarConsultaForm

def home(request):
	return render(request, 'SIGPAE/home.html', {})

def index(request):
	return render(request, 'SIGPAE/index.html', {})

def cargar_archivo(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(
				codigo = form.cleaned_data['codigo'],
				periodo = form.cleaned_data['periodo'],
				anio = form.cleaned_data['anio'],
				docfile = request.FILES['docfile'])
			newdoc.save()

			newhist = Historial(
				docfile_id = newdoc)
			newhist.save()
			'''
			opcion = form.cleaned_data['tipo']
			if (opcion == "texto"):
				texto_editable = textract.process(newdoc.docfile.url)
			else:
				os.system("pdftohtml -s -c " + newdoc.docfile.url)
				output = re.sub('.(p|P)(d|D)(f|F)', '-html.html', newdoc.docfile.url)
				file = open(output, "r")
				texto_editable = file.read()
				file.close()
			context = {'texto_editable': texto_editable, 'documento': newdoc}
			'''
			return render(request, 'SIGPAE/cargar.html', {'form': DocumentForm()})
		return render(request,'SIGPAE/cargar.html',{'form': DocumentForm()})
	return render(request,'SIGPAE/cargar.html',{'form': DocumentForm()})

def transcripcion(request):
	if request.method == 'POST':
		pass
	if request.GET.items():
		opcion = request.GET['tipo']
		docfile = request.GET['documento']
		row = Historial.objects.all().filter(docfile_name = docfile)
		if (opcion == "texto"):
			texto_editable = textract.process(docfile)
		else:
			os.system("pdftohtml -s -c " + docfile)
			output = re.sub('.(p|P)(d|D)(f|F)', '-html.html', docfile)
			file = open(output, "r")
			texto_editable = file.read()
			file.close()

		context = {'texto_editable': texto_editable, 'row': row}
		return render(request, 'SIGPAE/transcripcion.html', context)
	else:
		form = DocumentForm()
		documents = Document.objects.all()
		return render(request,'SIGPAE/cargar.html',{'form': form})

def consulta(request):
	if request.method == 'POST':
		form = ConsultaForm(request.POST, request.FILES)
		if form.is_valid():

			cod = form.cleaned_data['codigo'],
			aux=str(cod).split("'")
			cod=aux[1]
			per = form.cleaned_data['periodo'],
			aux = str(per).split("'")
			per=aux[1]
			an = form.cleaned_data['anio']

			if(per==str(0) or an==str(0)):
				doc = Document.objects.filter(codigo=cod).order_by('-periodo' and '-anio')
				if doc:
					form = MostrarConsultaForm()
					context = {'documents': doc,'cod':cod,'form':form}
					return render(request,'SIGPAE/mostrarConsulta.html',context)

				else:
					mensaje="No hay archivos con esas especificaciones"
					form = ConsultaForm()
					return render(request,'SIGPAE/consulta.html',{'form': form, 'mensaje':mensaje})

			else:
				doc = Document.objects.filter(codigo=cod, periodo=per, anio=an)

				if doc:
					for f in doc:
						nombre = os.path.basename(f.docfile.name)
						texto_editable = textract.process(f.docfile.url)
						context = {'texto_editable': texto_editable, 'documento': f}
						return render(request, 'SIGPAE/transcripcion.html', context)

				else:
					doc = Document.objects.filter(codigo=cod).order_by('-periodo' and '-anio')
					if doc:
						form = MostrarConsultaForm()
						context = {'documents': doc,'cod':cod,'form':form}
						return render(request, 'SIGPAE/mostrarConsulta.html', context)
					else:
						mensaje = "No hay archivos con esas especificaciones"
						form = ConsultaForm()
						return render(request, 'SIGPAE/consulta.html', {'form': form, 'mensaje': mensaje})
	else:
		form=ConsultaForm()
		return render(request, 'SIGPAE/consulta.html', {'form': form})
