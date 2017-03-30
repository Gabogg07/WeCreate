# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
import textract
import os
import re

from .codigos import *
from .models import Document, Historial
from .forms import DocumentForm, ConsultaForm, HistorialForm, MostrarConsultaForm

def prueba(request,url):
	with open(url, 'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline;filename=some_file.pdf'
		return response
	pdf.closed

def home(request):
	context = {}
	if request.method == 'POST':
		form = HistorialForm(request.POST, request.FILES)
		if form.is_valid():
			if (form.cleaned_data['codigo_asignatura'].encode('UTF-8') != "" and
				form.cleaned_data['periodo'].encode('UTF-8') != "" and
				form.cleaned_data['anio'].encode('UTF-8') != ""):

				items = Historial.objects.all().filter(
						codigo_asignatura=form.cleaned_data['codigo_asignatura'],
						periodo=form.cleaned_data['periodo'],
						anio=form.cleaned_data['anio'])

				if items.count() > 0:
					message = "Introdujo un programa con código, período y año existentes"
					context = {'message':message}

			documento = request.POST['documento']
			row_hist = Historial.objects.all().filter(docfile_id = documento).first()
			row_hist.dependencia = form.cleaned_data['dependencia']
			row_hist.decanato = form.cleaned_data['decanato']
			row_hist.coordinacion_D1 = form.cleaned_data['coordinacion_D1']
			row_hist.coordinacion_D2 = form.cleaned_data['coordinacion_D2']
			row_hist.coordinacion_D3 = form.cleaned_data['coordinacion_D3']
			row_hist.division = form.cleaned_data['division']
			row_hist.departamento_D1 = form.cleaned_data['departamento_D1']
			row_hist.departamento_D2 = form.cleaned_data['departamento_D2']
			row_hist.departamento_D3 = form.cleaned_data['departamento_D3']
			row_hist.departamento_D4 = form.cleaned_data['departamento_D4']
			row_hist.codigo_asignatura = form.cleaned_data['codigo_asignatura']
			row_hist.denominacion = form.cleaned_data['denominacion']
			row_hist.periodo = form.cleaned_data['periodo']
			row_hist.anio = form.cleaned_data['anio']
			row_hist.horas_T = form.cleaned_data['horas_T']
			row_hist.horas_P = form.cleaned_data['horas_P']
			row_hist.horas_L = form.cleaned_data['horas_L']
			row_hist.num_creditos = form.cleaned_data['num_creditos']
			row_hist.requisitos = form.cleaned_data['requisitos']
			row_hist.estrategias_met = form.cleaned_data['estrategias_met']
			row_hist.estrategias_ev = form.cleaned_data['estrategias_ev']
			row_hist.contenido = form.cleaned_data['contenido']
			row_hist.objetivos_generales = form.cleaned_data['objetivos_generales']
			row_hist.objetivos_especificos = form.cleaned_data['objetivos_especificos']
			row_hist.fuentes_info = form.cleaned_data['fuentes_info']
			x = form.cleaned_data['codigo_asignatura']
			x = x[:2].lower()
			if x in cods:
				temp0 = form.cleaned_data['departamento_D1'].encode('UTF-8')
				temp1 = form.cleaned_data['departamento_D2'].encode('UTF-8')
				temp2 = form.cleaned_data['departamento_D3'].encode('UTF-8')
				temp3 = form.cleaned_data['departamento_D4'].encode('UTF-8')
				if ( temp0 == cods[x] or temp1 == cods[x] or temp2 == cods[x] or temp3 == cods[x] ):

					row_hist.save()
					return render(request, 'SIGPAE/home.html', context)
				else:
					x = form.cleaned_data['codigo_asignatura'].encode('UTF-8')
					doc = Document.objects.filter(codigo=x).first()
					print("\n")
					print(doc.nombre)
					print("\n")

					id_row = Document.objects.all().filter(docfile = doc.docfile).first()
					row = Historial.objects.all().filter(docfile_id = id_row.id).first()
					print("\n")
					print(row.dependencia)
					print("\n")
					texto_editable = textract.process(doc.docfile.url)
					mensaje_alerta = "El código de la materia y el departamento no coinciden, por favor revisar"
					context = {'texto_editable': texto_editable, 'row':row, 'form':HistorialForm(), 'mensaje_alerta':mensaje_alerta}
					return render(request, 'SIGPAE/transcripcion.html', context)
			else:
				row_hist.save()
				return render(request, 'SIGPAE/home.html', context)

	elif (request.method == 'GET'):
		return render(request, 'SIGPAE/home.html', context)

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
				nombre=request.FILES['docfile'].name,
				docfile = request.FILES['docfile'])
			newdoc.save()

			newhist = Historial(
				docfile_id = newdoc)
			newhist.save()

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
			if re.search(r'csa', cdg): dpto = 'Departamento de Ciencias Sociales'
			if re.search(r'lla', cdg): dpto = 'Departamento de Lengua y Literatura'
			context = {'texto_editable': texto_editable, 'documento': newdoc.docfile, 'codigo': cdg.upper(),'dpto':dpto,'row': newhist, 'form':HistorialForm()}
			return render(request, 'SIGPAE/transcripcion.html', context)
		return render(request,'SIGPAE/cargar.html',{'form': form})
	return render(request,'SIGPAE/cargar.html',{'form': DocumentForm()})

def transcripcion(request):
	if request.GET.items():
		opcion = request.GET['tipo']
		docfile = request.GET['documento']
		#print ("\n" + docfile + "\n")
		ruta = request.GET['ruta']
		id_row = Document.objects.all().filter(docfile = docfile).first()
		#print(request.GET['row'])
		'''if 'row' in request.GET:
			print("LIDHCIHD")
			row = request.GET['row']
		else:
			print ("\n")
			print("ESTOY ES AQUI")
			print ("\n")'''
		row = Historial.objects.all().filter(docfile_id = id_row.id).first()


		if (opcion == "texto"):
			texto_editable = textract.process(docfile)
			texto_editable=texto_editable.decode("utf-8")
			match = re.findall(r'(((co|ep|dfm|et|ci|bc|bo|mt|gc|ce|cs|cc|ct|da|ec|ea|ff|fl|fs|fis|fc|id|ll|ma|mc|pl|ps|qm|pb|ts|ti|tf|fc|pg|td|tg)(-|\s)?([0-9][0-9][0-9][0-9]))|((dfm|cib|bcb|bob|cmt|cea|csa|csx|csy|csz|egs|cce|cte|dap|daa|eyc|ead|fsi|fis|fcr|fca|fcb|fcc|fce|fcf|fcg|fch|fci|fcl|fcr|fcx|fcz|fcw|idm|lla|llb|llc|lle|egl|mat|mec|plx|ply|prs|qim|tsx|tft|teg)(-|\s)?([0-9][0-9][0-9])))',texto_editable.lower())
			if match: match=match[0]
			else: match=""
			cdg=""
			if match:
				cdg=match[0]
		else:
			os.system("pdftohtml -s -c " + docfile)
			output = re.sub('.(p|P)(d|D)(f|F)', '-html.html', docfile)
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
		if re.search(r'csa', cdg): dpto = 'Departamento de Ciencias Sociales'
		if re.search(r'lla', cdg): dpto = 'Departamento de Lengua y Literatura'
		context = {'texto_editable': texto_editable, 'ruta': ruta, 'codigo': cdg.upper(),'dpto':dpto,'row': row,'form':HistorialForm()}
		return render(request, 'SIGPAE/transcripcion.html', context)
	else:
		form = DocumentForm()
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
					print("ENTRE EN ESTE ID DE doc")
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
						print("este es el de consulta" + "\n")
						print(f)
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
