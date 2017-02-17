from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import textract

from .models import Document
from .forms import DocumentForm

def index(request):
	context = {}
	return render(request, 'SIGPAE/index.html', context)

def upload_file(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile=request.FILES['docfile'])
			newdoc.save()

			texto_editable = textract.process(newdoc.docfile.url)
			context = {'texto_editable': texto_editable,}
			return render(request, 'SIGPAE/index.html', context)
	else:
		form = DocumentForm()

	documents = Document.objects.all()

	return render(request,'SIGPAE/upload.html',{'documents': documents, 'form': form})