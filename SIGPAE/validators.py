# -*- coding: utf-8 -*-

def validar_extension(value):
	import os
	from django.core.exceptions import ValidationError
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.pdf']
	if not ext.lower() in valid_extensions:
		raise ValidationError(u'El archivo no es PDF')