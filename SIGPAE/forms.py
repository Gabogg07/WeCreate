# -*- coding: utf-8 -*-

from django import forms
from django.forms import Textarea
from .validators import validar_extension, validar_unicidad
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

	docfile = forms.FileField(label='Selecciona un archivo PDF', validators=[validar_extension,validar_unicidad])

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
	DEPENDENCIA = [
			('Coordinación', 'Coordinación'),
			('Departamento', 'Departamento')]

	DEPENDENCIA.insert(0, (0, 'Sin seleccionar'))

	DECANATO = [
			('Decanato de Estudios Generales', 'Decanato de Estudios Generales'),
			('Decanato de Estudios Profesionales', 'Decanato de Estudios Profesionales'),
			('Decanato de Estudios Tecnológicos', 'Decanato de Estudios Tecnológicos')]

	DECANATO.insert(0, (0, 'Sin seleccionar'))

	COORDINACION_D1 = [
				('Coordinación del Ciclo Básico', 'Coordinación del Ciclo Básico'),
				('Coordinación del Ciclo Profesional', 'Coordinación del Ciclo Profesional'),
				('Coordinación de Formación General', 'Coordinación de Formación General'),
				('Coordinación del Ciclo de Iniciación Universitaria', 'Coordinación del Ciclo de Iniciación Universitaria')]

	COORDINACION_D1.insert(0, (0, 'Sin seleccionar'))

	COORDINACION_D2 = [
				('Coordinación de Química', 'Coordinación de Química'),
				('Coordinación de Matemática', 'Coordinación de Matemática'),
				('Coordinación de Biología', 'Coordinación de Biología'),
				('Coordinación de Física', 'Coordinación de Física'),
				('Coordinación de Tecnología e Ingeniería Eléctrica', 'Coordinación de Tecnología e Ingeniería Eléctrica'),
				('Coordinación de Tecnología e Ingeniería Electrónica', 'Coordinación de Tecnología e Ingeniería Electrónica'),
				('Coordinación de Ingeniería Mecánica', 'Coordinación de Ingeniería Mecánica'),
				('Coordinación de Ingeniería Química', 'Coordinación de Ingeniería Química'),
				('Coordinación de Ingeniería de Computación', 'Coordinación de Ingeniería de Computación'),
				('Coordinación de Ingeniería Geofísica', 'Coordinación de Ingeniería Geofísica'),
				('Coordinación de Ingeniería de Materiales', 'Coordinación de Ingeniería de Materiales'),
				('Coordinación de Ingeniería de Producción y Organización Empresarial', 'Coordinación de Ingeniería de Producción y Organización Empresarial'),
				('Coordinación de Tecnología Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento', 'Coordinación de Tecnología Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento'),
				('Coordinación de Ingeniería de Telecomunicaciones', 'Coordinación de Ingeniería de Telecomunicaciones'),
				('Coordinación de Arquitectura', 'Coordinación de Arquitectura'),
				('Coordinación de Estudios Urbanos', 'Coordinación de Estudios Urbanos'),
				('Coordinación de Turismo, Hotelería y Hospitalidad', 'Coordinación de Turismo, Hotelería y Hospitalidad'),
				('Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional', 'Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional')]
	COORDINACION_D2.insert(0, (0, 'Sin seleccionar'))

	COORDINACION_D3 = [
				('Coordinación de Tecnología e Ingeniería Eléctrica', 'Coordinación de Tecnología e Ingeniería Eléctrica'),
				('Coordinación de Tecnología Eléctrica y Electrónica', 'Coordinación de Tecnología Eléctrica y Electrónica'),
				('Coordinación de Ingeniería de Producción y Organización Empresarial', 'Coordinación de Ingeniería de Producción y Organización Empresarial'),
				('Coordinación de Turismo, Hotelería y Hospitalidad', 'Coordinación de Turismo, Hotelería y Hospitalidad'),
				('Coordinación de Administración Aduanera', 'Coordinación de Administración Aduanera'),
				('Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional', 'Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional'),
				('Coordinación de Administración del Transporte y Organización Empresarial', 'Coordinación de Administración del Transporte y Organización Empresarial'),
				('Coordinación de Tecnología Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento', 'Coordinación de Tecnología Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento')]
	COORDINACION_D3.insert(0, (0, 'Sin seleccionar'))

	DIVISION = [
		('División de Ciencias Físicas y Matemáticas', 'División de Ciencias Físicas y Matemáticas'),
		('División de Ciencias Sociales y Humanidades', 'División de Ciencias Sociales y Humanidades'),
		('División de Ciencias Biológicas', 'División de Ciencias Biológicas'),
		('División de Ciencias y Tecnologías Administrativas e Industriales', 'División de Ciencias y Tecnologías Administrativas e Industriales')]

	DIVISION.insert(0, (0, 'Sin seleccionar'))

	DEPARTAMENTO_1 = [
			('Departamento de Física', 'Departamento de Física'),
			('Departamento de Química', 'Departamento de Química'),
			('Departamento de Mecánica', 'Departamento de Mecánica'),
			('Departamento de Matemáticas Puras y Aplicadas', 'Departamento de Matemáticas Puras y Aplicadas'),
			('Departamento de Computación y Tecnología de la Información', 'Departamento de Computación y Tecnología de la Información'),
			('Departamento de Cómputo Científico y Estadística', 'Departamento de Cómputo Científico y Estadística'),
			('Departamento de Electrónica y Circuitos', 'Departamento de Electrónica y Circuitos'),
			('Departamento de Termodinámica y Fenómenos de Transferencia', 'Departamento de Termodinámica y Fenómenos de Transferencia'),
			('Departamento de Conversión y Transporte de Energía', 'Departamento de Conversión y Transporte de Energía'),
			('Departamento de Procesos y Sistemas', 'Departamento de Procesos y Sistemas'),
			('Departamento de Ciencias de los Materiales', 'Departamento de Ciencias de los Materiales'),
			('Departamento de Ciencias de la Tierra', 'Departamento de Ciencias de la Tierra')]

	DEPARTAMENTO_1.insert(0, (0, 'Sin seleccionar'))

	DEPARTAMENTO_2 = [
			('Departamento de Ciencia y Tecnología del Comportamiento', 'Departamento de Ciencia y Tecnología del Comportamiento'),
			('Departamento de Lengua y Literatura', 'Departamento de Lengua y Literatura'),
			('Departamento de Ciencias Económicas y Administrativas', 'Departamento de Ciencias Económicas y Administrativas'),
			('Departamento de Idiomas', 'Departamento de Idiomas'),
			('Departamento de Filosofía', 'Departamento de Filosofía'),
			('Departamento de Ciencias Sociales', 'Departamento de Ciencias Sociales'),
			('Departamento de Diseño Arquitectura y Artes Plásticas', 'Departamento de Diseño Arquitectura y Artes Plásticas'),
			('Departamento de Planificación Urbana', 'Departamento de Planificación Urbana')]

	DEPARTAMENTO_2.insert(0, (0, 'Sin seleccionar'))

	DEPARTAMENTO_3 = [
			('Departamento de Biología Celular', 'Departamento de Biología Celular'),
			('Departamento de Estudios Ambientales', 'Departamento de Estudios Ambientales'),
			('Departamento de Biología de Organismos', 'Departamento de Biología de Organismos'),
			('Departamento de Tecnología de Procesos Biológicos y Bioquímicos', 'Departamento de Tecnología de Procesos Biológicos y Bioquímicos')]

	DEPARTAMENTO_3.insert(0, (0, 'Sin seleccionar'))

	DEPARTAMENTO_4 = [
			('Departamento de Tecnología de Servicios', 'Departamento de Tecnología de Servicios'),
			('Departamento de Tecnología Industrial', 'Departamento de Tecnología Industrial'),
			('Departamento de Formación General y Ciencias Básicas', 'Departamento de Formación General y Ciencias Básicas')]

	DEPARTAMENTO_4.insert(0, (0, 'Sin seleccionar'))

	PERIODOS = [
		('Sep-Dic','Sep-Dic'),
		('Ene-Mar','Ene-Mar'),
		('Abr-Jul','Abr-Jul'),
		('Intensivo','Intensivo')]

	PERIODOS.insert(0,(0,'Sin seleccionar'))

	CONTENIDO = [
		('Objetivos','Objetivos'),
		('Objetivos Generales y Específicos','Objetivos Generales y Específicos')]

	CONTENIDO.insert(0,(0,'Sin seleccionar'))

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

	dependencia = forms.ChoiceField(choices=DEPENDENCIA, label="Dependencia", required = False)
	decanato = forms.ChoiceField(choices=DECANATO, label="Decanato", required = False)
	coordinacion_D1 = forms.ChoiceField(choices=COORDINACION_D1, label="Coordinación 1", required = False)
	coordinacion_D2 = forms.ChoiceField(choices=COORDINACION_D2, label="Coordinación 2", required = False)
	coordinacion_D3 = forms.ChoiceField(choices=COORDINACION_D3, label="Coordinación 3", required = False)
	division = forms.ChoiceField(choices=DIVISION, label="División", required = False)
	departamento_D1 = forms.ChoiceField(choices=DEPARTAMENTO_1, label="Departamento 1", required = False)
	departamento_D2 = forms.ChoiceField(choices=DEPARTAMENTO_2, label="Departamento 2", required = False)
	departamento_D3 = forms.ChoiceField(choices=DEPARTAMENTO_3, label="Departamento 3", required = False)
	departamento_D4 = forms.ChoiceField(choices=DEPARTAMENTO_4, label="Departamento 4", required = False)

	codigo_asignatura = forms.CharField(label="Código", required = False)
	denominacion = forms.CharField(label="Denominación", required = False)
	periodo = forms.ChoiceField(choices=PERIODOS, label="Período", required = False)
	anio = forms.ChoiceField(choices=ANIOS, label="Año", required = False)
	horas_T = forms.ChoiceField(choices=HORAS_T, label="Horas de Teoría", required = False)
	horas_P = forms.ChoiceField(choices=HORAS_P, label="Horas de Práctica", required = False)
	horas_L = forms.ChoiceField(choices=HORAS_L, label="Horas de Laboratorio", required = False)
	num_creditos = forms.ChoiceField(choices=CREDITOS, label="Número de Créditos", required = False)
	requisitos = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 6}), label="Requisitos", required = False)
	estrategias_met = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 6}), label="Estrategias Metodológicas", required = False)
	estrategias_ev = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 6}), label="Estrategias de Evaluación", required = False)
	contenido = forms.ChoiceField(choices=CONTENIDO, label="Seleccione el tipo de contenido", required = False)
	objetivos_generales = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 6}), label="Objetivos Generales", required = False)
	objetivos_especificos = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 6}), label="Objetivos Específicos", required = False)
	fuentes_info = forms.CharField(widget=forms.Textarea(attrs={'cols': 25, 'rows': 6}), label="Fuentes de Información recomendadas", required = False)
