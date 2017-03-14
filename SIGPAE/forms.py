# -*- coding: utf-8 -*-

from django import forms
from django.forms import Textarea
from .validators import validar_extension
import datetime

class DocumentForm(forms.Form):
	PERIODOS = [
		('Sep-Dic','Sep-Dic'),
		('Ene-Mar','Ene-Mar'),
		('Abr-Jul','Abr-Jul'),
		('Intensivo','Intensivo')]

	PERIODOS.insert(0,(0,'Sin seleccionar'))

	ANIOS = [(x, x) for x in range(1969, datetime.datetime.now().year+1)]

	ANIOS.insert(0,(0,'Sin seleccionar'))

	TIPO = [
		('texto','Texto'),
		('html','HTML')]

	codigo = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}),label="Código")

	periodo = forms.ChoiceField(choices=PERIODOS,label="Período")

	anio = forms.ChoiceField(choices=ANIOS,label="Año")

	tipo = forms.ChoiceField(choices=TIPO, label="Tipo de transcripción")

	docfile = forms.FileField(label='Selecciona un archivo PDF', validators=[validar_extension])

class ConsultaForm(forms.Form):
	PERIODOS = [
		('Sep-Dic', 'Sep-Dic'),
		('Ene-Mar', 'Ene-Mar'),
		('Abr-Jul', 'Abr-Jul'),
		('Intensivo', 'Intensivo')]

	PERIODOS.insert(0, (0, 'Sin seleccionar'))

	ANIOS = [(x, x) for x in range(1969, datetime.datetime.now().year + 1)]

	ANIOS.insert(0, (0, 'Sin seleccionar'))

	TIPO = [
		('texto','Texto'),
		('html','HTML')]

	codigo = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Código")

	periodo = forms.ChoiceField(choices=PERIODOS, label="Período")

	anio = forms.ChoiceField(choices=ANIOS, label="Año")

class MostrarConsultaForm(forms.Form):
	TIPO = [
		('texto','Texto'),
		('html','HTML')]

	tipo = forms.ChoiceField(choices=TIPO, label="Tipo de transcripción")


class HistorialForm(forms.Form):
	PERIODOS = [
		('Sep-Dic', 'Sep-Dic'),
		('Ene-Mar', 'Ene-Mar'),
		('Abr-Jul', 'Abr-Jul'),
		('Intensivo', 'Intensivo')]

	PERIODOS.insert(0, (0, 'Sin seleccionar'))

	ANIOS = [(x, x) for x in range(1969, datetime.datetime.now().year + 1)]

	ANIOS.insert(0, (0, 'Sin seleccionar'))

	CREDITOS = [(x, x) for x in range(1, 17)]

	CREDITOS.insert(0, (0, 'Sin seleccionar'))

	codigo_asignatura = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Código")
