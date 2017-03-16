# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
	codigo = models.CharField(max_length=10,default="")
	periodo = models.CharField(max_length=10,default="")
	anio = models.IntegerField(default=0)
	nombre = models.CharField(max_length=1024,default="")
	docfile = models.FileField(upload_to='documents')
