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

def prueba(request):
	with open('/home/gabriel/PycharmProjects/WeCreate/documents/LLA-111.pdf', 'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline;filename=some_file.pdf'
		return response
	pdf.closed

def home(request):
	if request.method == 'POST':
		print("\nPOST\n")
		form = HistorialForm(request.POST, request.FILES)
		if form.is_valid():
			print("\nFORM VALIDO\n")
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
			row_hist.cont_sinopticos = form.cleaned_data['cont_sinopticos']
			row_hist.estrategias_met = form.cleaned_data['estrategias_met']
			row_hist.estrategias_ev = form.cleaned_data['estrategias_ev']
			row_hist.objetivos = form.cleaned_data['objetivos']
			row_hist.fuentes_info = form.cleaned_data['fuentes_info']
			row_hist.save()

	return render(request, 'SIGPAE/home.html', {})

def index(request):
	return render(request, 'SIGPAE/index.html', {})

def cargar_archivo(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			print("Form valido")
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
			context = {'texto_editable': texto_editable, 'documento': newdoc, 'codigo': cdg.upper(),'dpto':dpto,'row': newhist, 'form':HistorialForm()}
			return render(request, 'SIGPAE/transcripcion.html', context)
		return render(request,'SIGPAE/cargar.html',{'form': form})
	return render(request,'SIGPAE/cargar.html',{'form': DocumentForm()})

def transcripcion(request):
	if request.GET.items():
		opcion = request.GET['tipo']
		docfile = request.GET['documento']
		id_row = Document.objects.all().filter(docfile = docfile).first()
		row = Historial.objects.all().filter(docfile_id = id_row.id).first()
		if (opcion == "texto"):
			texto_editable = textract.process(docfile)
		else:
			os.system("pdftohtml -s -c " + docfile)
			output = re.sub('.(p|P)(d|D)(f|F)', '-html.html', docfile)
			file = open(output, "r")
			texto_editable = file.read()
			file.close()

		context = {'texto_editable': texto_editable, 'row': row, 'form':HistorialForm()}
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
