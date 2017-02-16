from django.shortcuts import render

import textract

def index(request):
	#texto_editable = "Este es el texto que quiero editar"
	texto_editable = textract.process('/home/julio/prueba.pdf')

	context = {'texto_editable': texto_editable,}
	return render(request, 'SIGPAE/index.html', context)
