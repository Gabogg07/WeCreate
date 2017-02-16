from django.shortcuts import render

def index(request):
	texto_editable = "Este es el texto que quiero editar"
	context = {'texto_editable': texto_editable,}
	return render(request, 'SIGPAE/index.html', context)