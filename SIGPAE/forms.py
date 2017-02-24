# -*- coding: utf-8 -*-

from django import forms
from django.forms import Textarea
from .validators import validar_extension
import datetime

class DocumentForm(forms.Form):
	PERIODOS = [
		('sep-dic','sep-dic'),
		('ene-mar','ene-mar'),
		('abr-jul','abr-jul'),
		('intensivo','intensivo')]

	ANIOS = [(x, x) for x in range(1969, datetime.datetime.now().year+1)]

	ANIOS.insert(0,(0,'Sin seleccionar'))

	codigo = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}),label="Código")

	periodo = forms.ChoiceField(choices=PERIODOS,label="Período")

	anio = forms.ChoiceField(choices=ANIOS,label="Año")

	docfile = forms.FileField(label='Selecciona un archivo PDF', validators=[validar_extension])