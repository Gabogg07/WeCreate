# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
	codigo = models.CharField(max_length=10,default="")
	periodo = models.CharField(max_length=10,default="")
	anio = models.IntegerField(default=0)
	docfile = models.FileField(upload_to='documents')


class Historial(models.Model):
    codigo_asignatura = models.CharField(max_length = 512, default = "")
    denominacion = models.CharField(max_length = 512, default = "")
    periodo = models.CharField(max_length = 512, default = "")
    anio = models.IntegerField(default = 0)
    horas_T = models.IntegerField(default = 0)
    horas_P = models.IntegerField(default = 0)
    horas_L = models.IntegerField(default = 0)
    num_creditos = models.IntegerField(default = 0)
    requisitos = models.CharField(max_length = 512, default = "")
    cont_sinopticos = models.CharField(max_length = 512, default = "")
    estrategias_met = models.CharField(max_length = 512, default = "")
    estrategias_ev = models.CharField(max_length = 512, default = "")
    objetivos = models.CharField(max_length = 512, default = "")
    fuentes_info = models.CharField(max_length = 512, default = "")
    docfile_id = models.ForeignKey('Document')
