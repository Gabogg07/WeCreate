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

	HORAS_T = [(x, x) for x in range(1, 42)]

	HORAS_T.insert(0, (0, 'Sin seleccionar'))

	HORAS_P = [(x, x) for x in range(1, 42)]

	HORAS_P.insert(0, (0, 'Sin seleccionar'))

	HORAS_L = [(x, x) for x in range(1, 42)]

	HORAS_L.insert(0, (0, 'Sin seleccionar'))


	codigo_asignatura = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Código", required = False)
	denominacion = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Denominación", required = False)
	periodo = forms.ChoiceField(choices=PERIODOS, label="Período", required = False)
	anio = forms.ChoiceField(choices=ANIOS, label="Año", required = False)
	horas_T = forms.ChoiceField(choices=HORAS_T, label="Horas de Teoría", required = False)
	horas_P = forms.ChoiceField(choices=HORAS_P, label="Horas de Práctica", required = False)
	horas_L = forms.ChoiceField(choices=HORAS_L, label="Horas de Laboratorio", required = False)
	num_creditos = forms.ChoiceField(choices=CREDITOS, label="Número de Créditos", required = False)
	requisitos = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Requisitos", required = False)
	cont_sinopticos = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Contenidos Sinópticos", required = False)
	estrategias_met = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Estrategias Metodológicas", required = False)
	estrategias_ev = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Estrategias de Evaluación", required = False)
	objetivos = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Objetivos", required = False)
	fuentes_info = forms.CharField(widget=forms.Textarea(attrs={'cols': 10, 'rows': 1}), label="Fuentes de Información recomendadas", required = False)
