# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import textract
import os
import re

from .codigos import *
from .models import *
from .forms import DocumentForm, ConsultaForm, HistorialForm, MostrarConsultaForm

def prueba(request,url):
	with open(url, 'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline;filename=some_file.pdf'
		return response
	pdf.closed

'''
Esta función se encarga de guardar en la base de datos la transcripción que se este realizando de
un programa en caso de que el metodo con el que se llame sea el POST

En caso de que se llame a 'home' con el metodo GET sencillamente te envía a la pagina principal de SIGPAE
'''
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
				#Se verifica que no haya un programa con el mismo codigo año y periodo iguales
				if items.count() > 0:
					message = "Introdujo un programa con código, período y año existentes"
					context = {'message':message}

			documento = request.POST['documento']

			#Query que instancia el documento que se va a transcribir
			row_hist = Historial.objects.all().filter(docfile_id = documento).first()

			#Cada campo se guarda en la base de datosen la tabla Historial
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

			#Se verifica si el código introducido coincide con el departamento
			x = form.cleaned_data['codigo_asignatura']
			x = x[:2].lower()
			if x in cods:
				temp0 = form.cleaned_data['departamento_D1'].encode('UTF-8')
				temp1 = form.cleaned_data['departamento_D2'].encode('UTF-8')
				temp2 = form.cleaned_data['departamento_D3'].encode('UTF-8')
				temp3 = form.cleaned_data['departamento_D4'].encode('UTF-8')
				#Si coincide el codigo con el departamento, se guarda
				if ( temp0 == cods[x] or temp1 == cods[x] or temp2 == cods[x] or temp3 == cods[x] ):

					row_hist.save()
					return render(request, 'SIGPAE/home.html', context)
				#Si no coincide, se recarga la página con un alert
				else:
					doc = Document.objects.all().filter(id = documento).first()
					row = Historial.objects.all().filter(docfile_id = documento).first()
					cdg = request.POST['cod']
					print cdg
					dpto = request.POST['dpto']
					print dpto
					texto_editable = textract.process(doc.docfile.url)
					mensaje_alerta = "El código de la materia y el departamento no coinciden, por favor revisar"
					context = {'texto_editable': texto_editable, 'documento': doc.docfile, 'codigo': cdg.upper(), 'dpto':dpto, 'row':row, 'form':HistorialForm(), 'mensaje_alerta':mensaje_alerta}
					return render(request, 'SIGPAE/transcripcion.html', context)
			#Si se queda en blanco el campo del código, se guarda también
			elif (form.cleaned_data['codigo_asignatura'].encode('UTF-8') == ""):
				row_hist.save()
				return render(request, 'SIGPAE/home.html', context)
			#Si se coloca algo que no sea un codigo ni nada manda un mensaje de alerta que no coincide con el departamento
			#que este puesto
			else:
				doc = Document.objects.all().filter(id = documento).first()
				row = Historial.objects.all().filter(docfile_id = documento).first()
				cdg = request.POST['cod']
				dpto = request.POST['dpto']
				texto_editable = textract.process(doc.docfile.url)
				mensaje_alerta = "El código de la materia y el departamento no coinciden, por favor revisar"
				context = {'texto_editable': texto_editable, 'documento': doc.docfile, 'codigo': cdg.upper(), 'dpto':dpto, 'row':row, 'form':HistorialForm(), 'mensaje_alerta':mensaje_alerta}
				return render(request, 'SIGPAE/transcripcion.html', context)

	#Si se llama a 'home' con el metodo get, simplemente se muestra la página principal
	elif (request.method == 'GET'):
		return render(request, 'SIGPAE/home.html', context)

def index(request):
	return render(request, 'SIGPAE/index.html', {})

def base(request):
	return render(request, 'SIGPAE/base.html', {})

def cargar_archivo(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			myfile = request.FILES['docfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)

			newdoc = Document(
				codigo = form.cleaned_data['codigo'],
				periodo = form.cleaned_data['periodo'],
				anio = form.cleaned_data['anio'],
				nombre=request.FILES['docfile'].name,
				docfile = os.path.abspath(myfile.name))
			newdoc.save()

			newhist = Historial(
				codigo_asignatura = form.cleaned_data['codigo'],
				periodo = form.cleaned_data['periodo'],
				anio = form.cleaned_data['anio'],
				docfile_id = newdoc)
			newhist.save()

			opcion = form.cleaned_data['tipo']
			if (opcion == "texto"):
				texto_editable = textract.process(newdoc.docfile)
				texto_editable=texto_editable.decode("utf-8")
				match = re.findall(r'(((co|ep|dfm|et|ci|bc|bo|mt|gc|ce|cs|cc|ct|da|ec|ea|ff|fl|fs|fis|fc|id|ll|ma|mc|pl|ps|qm|pb|ts|ti|tf|fc|pg|td|tg)(-|\s)?([0-9][0-9][0-9][0-9]))|((dfm|cib|bcb|bob|cmt|cea|csa|csx|csy|csz|egs|cce|cte|dap|daa|eyc|ead|fsi|fis|fcr|fca|fcb|fcc|fce|fcf|fcg|fch|fci|fcl|fcr|fcx|fcz|fcw|idm|lla|llb|llc|lle|egl|mat|mec|plx|ply|prs|qim|tsx|tft|teg)(-|\s)?([0-9][0-9][0-9])))',texto_editable.lower())
				if match: match=match[0]
				else: match=""
				cdg=""
				if match:
					cdg=match[0]
			else:
				os.system("pdftohtml -s -c " + newdoc.docfile)
				output = re.sub('.(p|P)(d|D)(f|F)', '-html.html', newdoc.docfile)
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
		ruta = request.GET['ruta']
		if docfile == "":
			row = Historial.objects.all().filter(id = request.GET['historia_id']).first()
			context = {'row': row,'form':HistorialForm(),'sigpae':True}
			return render(request, 'SIGPAE/transcripcion.html', context)
		id_row = Document.objects.all().filter(docfile = docfile).first()


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
				hist = Historial.objects.filter(codigo_asignatura=cod).order_by('-periodo' and '-anio')
				if hist:
					form = MostrarConsultaForm()
					context = {'historias': hist,'cod':cod,'form':form}
					return render(request,'SIGPAE/mostrarConsulta.html',context)
				else:
					mensaje="No hay archivos con esas especificaciones"
					form = ConsultaForm()
					return render(request,'SIGPAE/consulta.html',{'form': form, 'mensaje':mensaje})	
			else:
				hist = Historial.objects.filter(codigo_asignatura=cod,periodo=per,anio=an).order_by('-periodo' and '-anio')
				if hist:
					form = MostrarConsultaForm()
					context = {'historias': hist,'cod':cod,'form':form}
					return render(request,'SIGPAE/mostrarConsulta.html',context)
				else:
					mensaje = "No hay archivos con esas especificaciones"
					form = ConsultaForm()
					return render(request, 'SIGPAE/consulta.html', {'form': form, 'mensaje': mensaje})
	else:
		form=ConsultaForm()
		return render(request, 'SIGPAE/consulta.html', {'form': form})

def transcripcion_sigpae(request):
	if request.GET.items():
		sol_id = request.GET['sol_id']
		solicitud = Solicitud.objects.using('gestionpae').filter(id=sol_id).first()
		programa = Programa.objects.using('gestionpae').filter(id=sol_id).first()

		newdoc = Document(
			codigo = solicitud.cod,
			periodo = programa.fecha_vigtrim,
			anio = programa.fecha_vigano,
			docfile = "")
		newdoc.save()

		newhist = Historial(
			codigo_asignatura = solicitud.cod,
			denominacion = solicitud.denominacion,
			periodo = programa.fecha_vigtrim,
			anio = programa.fecha_vigano,
			horas_T = programa.h_teoria,
			horas_P = programa.h_prac,
			horas_L = programa.h_lab,
			num_creditos = solicitud.creditos,
			requisitos = solicitud.requisito_cre,
			estrategias_met = programa.estrategias,
			estrategias_ev = programa.estrat_eval,
			contenido = programa.contenidos,
			objetivos_generales = programa.obj_g,
			objetivos_especificos = programa.obj_e,
			fuentes_info = programa.fuentes,
			docfile_id=newdoc)
			
		newhist.save()
		context = {'row': newhist, 'form': HistorialForm()}
		return render(request, 'SIGPAE/transcripcion_sigpae.html', context)
	elif request.method == 'POST':
		form = HistorialForm(request.POST, request.FILES)
		if form.is_valid():
			historia = request.POST['historia_id']
			row_hist = Historial.objects.all().filter(id = historia).first()
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
			row_hist.save()
		return render(request, 'SIGPAE/home.html', {})
	else:
		form = DocumentForm()
		return render(request,'SIGPAE/cargar.html',{'form': form})

def consulta_sigpae(request):
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
				solicitudes = Solicitud.objects.using('gestionpae').filter(cod=cod).order_by('-trime' and '-ano')
				if solicitudes:
					programas = Programa.objects.using('gestionpae').filter(id=solicitudes.first().id)
					form = MostrarConsultaForm()
					context = {'programas':programas, 'solicitud':solicitudes.first(), 'cod':cod, 'form':form}
					return render(request,'SIGPAE/mostrarSIGPAE.html',context)
				else:
					mensaje = "No hay programas con esas especificaciones"
					form = ConsultaForm()
					return render(request, 'SIGPAE/consulta_sigpae.html', {'form': form, 'mensaje': mensaje})

			'''		
				doc = Document.objects.filter(codigo=cod).order_by('-periodo' and '-anio')
				if doc:
					form = MostrarConsultaForm()
					context = {'documents': doc,'cod':cod,'form':form}
					return render(request,'SIGPAE/mostrarSIGPAE.html',context)

				else:
					mensaje="No hay archivos con esas especificaciones"
					form = ConsultaForm()
					return render(request,'SIGPAE/consulta_sigpae.html',{'form': form, 'mensaje':mensaje})

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
						return render(request, 'SIGPAE/mostrarSIGPAE.html', context)
					else:
						mensaje = "No hay archivos con esas especificaciones"
						form = ConsultaForm()
						return render(request, 'SIGPAE/consulta_sigpae.html', {'form': form, 'mensaje': mensaje})
			'''
	else:
		form=ConsultaForm()
		return render(request, 'SIGPAE/consulta_sigpae.html', {'form': form})
