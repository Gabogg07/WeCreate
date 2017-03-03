# -*- coding: utf-8 -*-

def validar_extension(value):
<<<<<<< HEAD
	import os
	from django.core.exceptions import ValidationError
	ext = os.path.splitext(value.name)[1]
	valid_extensions = ['.pdf']
	if not ext.lower() in valid_extensions:
		raise ValidationError(u'El archivo no es PDF')
=======
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Formato inválido')
>>>>>>> 139fc268705670d855abefb57ba379aecc65dedc
