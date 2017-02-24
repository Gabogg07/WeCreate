from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import textract

from .models import Document
from .forms import DocumentForm

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
				docfile = request.FILES['docfile'])
			newdoc.save()
			texto_editable = textract.process(newdoc.docfile.url)
			context = {'texto_editable': texto_editable, 'documento': newdoc}
			return render(request, 'SIGPAE/transcripcion.html', context)
	else:
		form = DocumentForm()
		documents = Document.objects.all()
		return render(request,'SIGPAE/cargar.html',{'documents': documents, 'form': form})