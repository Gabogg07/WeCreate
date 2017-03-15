# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
	codigo = models.CharField(max_length=10,default="")
	periodo = models.CharField(max_length=10,default="")
	anio = models.IntegerField(default=0)
	docfile = models.FileField(upload_to='documents')


class Historial(models.Model):
    codigo_asignatura = models.CharField(max_length = 512, default = "", null=True, blank=True)
    denominacion = models.CharField(max_length = 512, default = "", null=True, blank=True)
    periodo = models.CharField(max_length = 512, default = "Ningún Período", null=True, blank=True)
    anio = models.IntegerField(default = 0, null=True, blank=True)
    horas_T = models.IntegerField(default = 0, null=True, blank=True)
    horas_P = models.IntegerField(default = 0, null=True, blank=True)
    horas_L = models.IntegerField(default = 0, null=True, blank=True)
    num_creditos = models.IntegerField(default = 0, null=True, blank=True)
    requisitos = models.CharField(max_length = 512, default = "", null=True, blank=True)
    cont_sinopticos = models.CharField(max_length = 512, default = "", null=True, blank=True)
    estrategias_met = models.CharField(max_length = 512, default = "", null=True, blank=True)
    estrategias_ev = models.CharField(max_length = 512, default = "", null=True, blank=True)
    objetivos = models.CharField(max_length = 512, default = "", null=True, blank=True)
    fuentes_info = models.CharField(max_length = 512, default = "", null=True, blank=True)
    docfile_id = models.ForeignKey('Document')
