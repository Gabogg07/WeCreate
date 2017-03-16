from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
import textract
import os
import re

from .codigos import *
from .models import Document
from .forms import DocumentForm, ConsultaForm, MostrarConsultaForm

def prueba(request):
	with open('/home/gabriel/PycharmProjects/WeCreate/documents/LLA-111.pdf', 'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline;filename=some_file.pdf'
		return response
	pdf.closed

def home(request):
	return render(request, 'SIGPAE/home.html', {})

def index(request):
	return render(request, 'SIGPAE/index.html', {})

def cargar_archivo(request):
	form = DocumentForm()
	documents = Document.objects.all()
	return render(request,'SIGPAE/cargar.html',{'documents': documents, 'form': form})

def transcripcion(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(
				codigo = form.cleaned_data['codigo'],
				periodo = form.cleaned_data['periodo'],
				anio = form.cleaned_data['anio'],
				nombre=request.FILES['docfile'].name,
				docfile = request.FILES['docfile'])
			newdoc.save()
			opcion = form.cleaned_data['tipo']
			if (opcion == "texto"):
				texto_editable = textract.process(newdoc.docfile.url)
				texto_editable=texto_editable.decode("utf-8")
				match = re.findall(r'(((co|ep|dfm|et|ci|bc|bo|mt|gc|ce|cs|cc|ct|da|ec|ea|ff|fl|fs|fis|fc|id|ll|ma|mc|pl|ps|qm|pb|ts|ti|tf|fc|pg|td|tg)(-|\s)?([0-9][0-9][0-9][0-9]))|((dfm|cib|bcb|bob|cmt|cea|csa|csx|csy|csz|egs|cce|cte|dap|daa|eyc|ead|fsi|fis|fcr|fca|fcb|fcc|fce|fcf|fcg|fch|fci|fcl|fcr|fcx|fcz|fcw|idm|lla|llb|llc|lle|egl|mat|mec|plx|ply|prs|qim|tsx|tft|teg)(-|\s)?([0-9][0-9][0-9])))',texto_editable.lower())
				if match: match=match[0]
				else: match=""
				cdg=""
				if match:
					cdg=match[0]

			else:
				os.system("pdftohtml -s -c " + newdoc.docfile.url)
				output = re.sub('.(p|P)(d|D)(f|F)', '-html.html', newdoc.docfile.url)
				file = open(output, "r")
				texto_editable = file.read()
				file.close()
				match=[]
				cdg=""
			dpto=""
			codigo=""
			if match:
				if match[2] in cods:
					dpto = cods.get(match[2])
			with open('/home/gabriel/PycharmProjects/WeCreate/documents/MA-1112.pdf', 'rb') as pdf:
				response = HttpResponse(pdf.read(), content_type='application/pdf')
				response['Content-Disposition'] = 'inline;filename=some_file.pdf'
			context = {'texto_editable': texto_editable, 'documento': newdoc, 'codigo': cdg.upper(),'dpto':dpto,'url':response}
			return render(request, 'SIGPAE/transcripcion.html', context)
		return render(request,'SIGPAE/cargar.html',{'form': form})
	
	if request.GET.items():
		opcion = request.GET['tipo']
		docfile = request.GET['documento']
		if (opcion == "texto"):
			texto_editable = textract.process(docfile)

		else:
			os.system("pdftohtml -s -c " + docfile)
			output = re.sub('.(p|P)(d|D)(f|F)', '-html.html', docfile)
			file = open(output, "r")
			texto_editable = file.read()
			file.close()
		
		context = {'texto_editable': texto_editable}
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