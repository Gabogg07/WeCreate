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

	codigo = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Código")
	denominacion = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Denominación")
	periodo = forms.ChoiceField(choices=PERIODOS, label="Período")
	anio = forms.ChoiceField(choices=ANIOS, label="Año")
	horas_T = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Horas de Teoría")
	horas_P = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Horas de Práctica")
	horas_L = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Horas de Laboratorio")
	num_creditos = forms.ChoiceField(choices=CREDITOS, label="Número de Créditos")
	requisitos = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Requisitos")
	cont_sinopticos = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Contenidos Sinópticos")
	estrategias_met = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Estrategias Metodológicas")
	estrategias_ev = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Estrategias de Evaluación")
	objetivos = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Objetivos")
	fuentes_info = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Fuentes de Información recomendadas")

