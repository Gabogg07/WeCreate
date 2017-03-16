# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
	codigo = models.CharField(max_length=10,default="")
	periodo = models.CharField(max_length=10,default="")
	anio = models.IntegerField(default=0)
	nombre = models.CharField(max_length=1024,default="")
	docfile = models.FileField(upload_to='documents')

class Historial(models.Model):
    dependencia = models.CharField(max_length = 512, default = "", null=True)
    decanato = models.CharField(max_length = 512, default = "", null=True)
    coordinacion_D1 = models.CharField(max_length = 512, default = "", null=True)
    coordinacion_D2 = models.CharField(max_length = 512, default = "", null=True)
    coordinacion_D3 = models.CharField(max_length = 512, default = "", null=True)
    division = models.CharField(max_length = 512, default = "", null=True)
    departamento_D1 = models.CharField(max_length = 512, default = "", null=True)
    departamento_D2 = models.CharField(max_length = 512, default = "", null=True)
    departamento_D3 = models.CharField(max_length = 512, default = "", null=True)
    departamento_D4 = models.CharField(max_length = 512, default = "", null=True)
    codigo_asignatura = models.CharField(max_length = 512, default = "", null=True)
    denominacion = models.CharField(max_length = 512, default = "", null=True)
    periodo = models.CharField(max_length = 512, default = "", null=True)
    anio = models.IntegerField(default = 0, null=True)
    horas_T = models.IntegerField(default = 0, null=True)
    horas_P = models.IntegerField(default = 0, null=True)
    horas_L = models.IntegerField(default = 0, null=True)
    num_creditos = models.IntegerField(default = 0, null=True)
    requisitos = models.CharField(max_length = 512, default = "", null=True, blank=True)
    cont_sinopticos = models.CharField(max_length = 512, default = "", null=True, blank=True)
    estrategias_met = models.CharField(max_length = 512, default = "", null=True, blank=True)
    estrategias_ev = models.CharField(max_length = 512, default = "", null=True, blank=True)
    objetivos = models.CharField(max_length = 512, default = "", null=True, blank=True)
    fuentes_info = models.CharField(max_length = 512, default = "", null=True, blank=True)
    docfile_id = models.ForeignKey('Document')
