# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class Document(models.Model):
	codigo = models.CharField(max_length=10,default="")
	periodo = models.CharField(max_length=10,default="")
	anio = models.IntegerField(default=0)
	nombre = models.CharField(max_length=512,default="")
	docfile = models.CharField(max_length=2048,default="")

	class Meta:
		_DATABASE = 'default'
		db_table = 'document'

class Historial(models.Model):
	dependencia = models.CharField(max_length = 4557, default = "", null=True)
	decanato = models.CharField(max_length = 4557, default = "", null=True)
	coordinacion_D1 = models.CharField(max_length = 4557, default = "", null=True)
	coordinacion_D2 = models.CharField(max_length = 4557, default = "", null=True)
	coordinacion_D3 = models.CharField(max_length = 4557, default = "", null=True)
	division = models.CharField(max_length = 4557, default = "", null=True)
	departamento_D1 = models.CharField(max_length = 4557, default = "", null=True)
	departamento_D2 = models.CharField(max_length = 4557, default = "", null=True)
	departamento_D3 = models.CharField(max_length = 4557, default = "", null=True)
	departamento_D4 = models.CharField(max_length = 4557, default = "", null=True)
	codigo_asignatura = models.CharField(max_length = 4557, default = "", null=True)
	denominacion = models.CharField(max_length = 4557, default = "", null=True)
	periodo = models.CharField(max_length = 4557, default = "", null=True)
	anio = models.IntegerField(default = 0, null=True)
	horas_T = models.IntegerField(default = 0, null=True)
	horas_P = models.IntegerField(default = 0, null=True)
	horas_L = models.IntegerField(default = 0, null=True)
	num_creditos = models.IntegerField(default = 0, null=True)
	requisitos = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	estrategias_met = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	estrategias_ev = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	contenido = models.CharField(max_length = 4557, default = "Sin seleccionar", null=True)
	objetivos_generales = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	objetivos_especificos = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	fuentes_info = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	docfile_id = models.ForeignKey('Document')

	class Meta:
		_DATABASE = 'default'
		db_table = 'historial'

class Transcripcion(models.Model):
	dependencia = models.CharField(max_length = 4557, default = "", null=True)
	decanato = models.CharField(max_length = 4557, default = "", null=True)
	coordinacion_D1 = models.CharField(max_length = 4557, default = "", null=True)
	coordinacion_D2 = models.CharField(max_length = 4557, default = "", null=True)
	coordinacion_D3 = models.CharField(max_length = 4557, default = "", null=True)
	division = models.CharField(max_length = 4557, default = "", null=True)
	departamento_D1 = models.CharField(max_length = 4557, default = "", null=True)
	departamento_D2 = models.CharField(max_length = 4557, default = "", null=True)
	departamento_D3 = models.CharField(max_length = 4557, default = "", null=True)
	departamento_D4 = models.CharField(max_length = 4557, default = "", null=True)
	codigo_asignatura = models.CharField(max_length = 4557, default = "", null=True)
	denominacion = models.CharField(max_length = 4557, default = "", null=True)
	periodo = models.CharField(max_length = 4557, default = "", null=True)
	anio = models.IntegerField(default = 0, null=True)
	horas_T = models.IntegerField(default = 0, null=True)
	horas_P = models.IntegerField(default = 0, null=True)
	horas_L = models.IntegerField(default = 0, null=True)
	num_creditos = models.IntegerField(default = 0, null=True)
	requisitos = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	estrategias_met = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	estrategias_ev = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	contenido = models.CharField(max_length = 4557, default = "Sin seleccionar", null=True)
	objetivos_generales = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	objetivos_especificos = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	fuentes_info = models.CharField(max_length = 4557, default = "", null=True, blank=True)
	docfile_id = models.ForeignKey('Document')

	class Meta:
		_DATABASE = 'default'
		db_table = 'transcripcion'

class Asignatura(models.Model):
	codasig = models.CharField(primary_key=True, max_length=10)
	nombre = models.CharField(max_length=512)
	tipo = models.CharField(max_length=15)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'asignatura'


class Bitacora(models.Model):
	id = models.AutoField(primary_key=True)
	usbid = models.CharField(max_length=60)
	comentario = models.CharField(max_length=512)
	fecha = models.DateTimeField()

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'bitacora'
		unique_together = (('usbid', 'id', 'fecha', 'comentario'),)


class CampoImpartir(models.Model):
	nombre = models.CharField(primary_key=True, max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'campo_impartir'


class CampoNivel(models.Model):
	nombre = models.CharField(primary_key=True, max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'campo_nivel'


class Carrera(models.Model):
	codigo = models.CharField(primary_key=True, max_length=10)
	nombre = models.CharField(max_length=512)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'carrera'


class ClaseMateria(models.Model):
	nombre = models.CharField(primary_key=True, max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'clase_materia'


class Coordinacion(models.Model):
	usbid = models.CharField(primary_key=True, max_length=50)
	codcar = models.CharField(max_length=10, blank=True, null=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'coordinacion'


class Decanato(models.Model):
	usbid = models.CharField(primary_key=True, max_length=50)
	obligatorio = models.BooleanField()

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'decanato'


class Departamento(models.Model):
	usbid = models.CharField(primary_key=True, max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'departamento'


class Devueltosdace(models.Model):
	usbidda = models.CharField(max_length=50)
	usbidr = models.CharField(max_length=50)
	id = models.IntegerField()
	observacionesrd = models.CharField(max_length=512)
	num = models.AutoField(primary_key=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'devueltosdace'


class EsRequisito(models.Model):
	codpre = models.CharField(max_length=10)
	cod = models.CharField(max_length=10)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'es_requisito'
		unique_together = (('codpre', 'cod'),)


class Estudiante(models.Model):
	usbid = models.CharField(primary_key=True, max_length=50)
	cedula = models.CharField(max_length=20)
	tipo_estudiante = models.CharField(max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'estudiante'


class Generados(models.Model):
	fecha = models.DateField()
	nro_pag = models.IntegerField()
	nro_prog = models.IntegerField()

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'generados'


class Historico(models.Model):
	codasig = models.CharField(max_length=8)
	nomasig = models.CharField(max_length=512)
	trimestrei = models.CharField(max_length=8)
	anoi = models.IntegerField()
	trimestref = models.CharField(max_length=8, blank=True, null=True)
	anof = models.IntegerField(blank=True, null=True)
	ruta = models.CharField(max_length=512)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'historico'


class Profesor(models.Model):
	usbid = models.CharField(primary_key=True, max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'profesor'


class ProgTemp(models.Model):
	idprog = models.IntegerField()
	idtemp = models.IntegerField()
	idpla = models.IntegerField()

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'prog_temp'
		unique_together = (('idprog', 'idtemp', 'idpla'),)


class Programa(models.Model):
	h_teoria = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
	h_prac = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
	h_lab = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
	fecha_vigtrim = models.CharField(max_length=512, blank=True, null=True)
	fecha_vigano = models.IntegerField(blank=True, null=True)
	obj_g = models.CharField(max_length=512, blank=True, null=True)
	obj_e = models.CharField(max_length=512, blank=True, null=True)
	contenidos = models.CharField(max_length=512, blank=True, null=True)
	estrategias = models.CharField(max_length=512, blank=True, null=True)
	estrat_eval = models.CharField(max_length=512, blank=True, null=True)
	fuentes = models.CharField(max_length=512, blank=True, null=True)
	cronograma = models.CharField(max_length=512, blank=True, null=True)
	sinoptico = models.CharField(max_length=512, blank=True, null=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'programa'


class Programat(models.Model):
	h_teoria = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
	h_prac = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
	h_lab = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
	fecha_vigtrim = models.CharField(max_length=8, blank=True, null=True)
	fecha_vigano = models.IntegerField(blank=True, null=True)
	obj_g = models.CharField(max_length=512, blank=True, null=True)
	obj_e = models.CharField(max_length=512, blank=True, null=True)
	contenidos = models.CharField(max_length=512, blank=True, null=True)
	estrategias = models.CharField(max_length=512, blank=True, null=True)
	estrat_eval = models.CharField(max_length=512, blank=True, null=True)
	fuentes = models.CharField(max_length=512, blank=True, null=True)
	cronograma = models.CharField(max_length=512, blank=True, null=True)
	sinoptico = models.CharField(max_length=512, blank=True, null=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'programat'


class RBitPlan(models.Model):
	idplanilla = models.IntegerField()
	idbitacora = models.IntegerField()

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_bit_plan'
		unique_together = (('idplanilla', 'idbitacora'),)


class RCarMat(models.Model):
	codasig = models.CharField(max_length=8)
	codcar = models.CharField(max_length=10)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_car_mat'
		unique_together = (('codasig', 'codcar'),)


class RCoordPl(models.Model):
	usbid = models.CharField(max_length=50)
	id = models.IntegerField(primary_key=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_coord_pl'
		unique_together = (('usbid', 'id'),)


class RDecCoor(models.Model):
	usbiddec = models.CharField(max_length=50)
	usbidcoor = models.CharField(max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_dec_coor'
		unique_together = (('usbiddec', 'usbidcoor'),)


class RDecPl(models.Model):
	idplanilla = models.IntegerField()
	usbiddec = models.CharField(max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_dec_pl'
		unique_together = (('idplanilla', 'usbiddec'),)


class RDepPl(models.Model):
	idplanilla = models.IntegerField()
	usbidd = models.CharField(max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_dep_pl'
		unique_together = (('idplanilla', 'usbidd'),)


class REstHist(models.Model):
	usbid = models.CharField(max_length=50)
	id = models.IntegerField(primary_key=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_est_hist'
		unique_together = (('usbid', 'id'),)


class REstProg(models.Model):
	usbid = models.CharField(max_length=15)
	id = models.IntegerField(primary_key=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_est_prog'
		unique_together = (('usbid', 'id'),)


class RProfDep(models.Model):
	usbidp = models.CharField(max_length=50)
	usbidd = models.CharField(max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_prof_dep'
		unique_together = (('usbidp', 'usbidd'),)


class RProfPl(models.Model):
	usbid = models.CharField(max_length=50)
	id = models.IntegerField(primary_key=True)
	idplanilla = models.IntegerField()

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_prof_pl'
		unique_together = (('usbid', 'id'),)


class RProfTemp(models.Model):
	idtemp = models.IntegerField()
	usbid = models.CharField(max_length=30)
	idplanilla = models.IntegerField()

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_prof_temp'
		unique_together = (('idtemp', 'usbid'),)


class RProgPl(models.Model):
	idplanilla = models.IntegerField()
	idprograma = models.IntegerField()

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'r_prog_pl'
		unique_together = (('idplanilla', 'idprograma'),)


class Rechazadoscad(models.Model):
	usbidc = models.CharField(max_length=50)
	usbidd = models.CharField(max_length=50)
	id = models.IntegerField()
	observacionesrd = models.CharField(max_length=512)
	num = models.AutoField(primary_key=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'rechazadoscad'


class Rechazadosd(models.Model):
	usbidd = models.CharField(max_length=50)
	usbidp = models.CharField(max_length=50)
	id = models.IntegerField()
	observacionesrd = models.CharField(max_length=512)
	num = models.AutoField(primary_key=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'rechazadosd'


class Rechazadosdac(models.Model):
	usbidd = models.CharField(max_length=50)
	usbidc = models.CharField(max_length=50)
	id = models.IntegerField()
	observacionesrd = models.CharField(max_length=512)
	num = models.AutoField(primary_key=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'rechazadosdac'


class Rechazadosdecac(models.Model):
	usbiddec = models.CharField(max_length=50)
	usbidcor = models.CharField(max_length=50)
	id = models.IntegerField()
	observacionesrd = models.CharField(max_length=512)
	num = models.AutoField(primary_key=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'rechazadosdecac'


class Rechazadosp(models.Model):
	usbidd = models.CharField(max_length=50)
	usbidp = models.CharField(max_length=50)
	id = models.IntegerField()
	observacionesrd = models.CharField(max_length=512)
	num = models.AutoField(primary_key=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'rechazadosp'


class Solicitud(models.Model):
	nomcoord = models.CharField(max_length=50)
	porasignar = models.BooleanField()
	porvalidard = models.BooleanField()
	porrevisarp = models.BooleanField()
	rechazadoc = models.BooleanField()
	validadoc = models.BooleanField()
	enviadod = models.BooleanField()
	devueltodace = models.BooleanField()
	fechaelab = models.DateField()
	tipo_solicitud = models.CharField(max_length=20)
	subtipo_solicitud = models.CharField(max_length=30)
	nivel = models.CharField(max_length=20)
	cod = models.CharField(max_length=7)
	cod_anterior = models.CharField(max_length=7, blank=True, null=True)
	denominacion = models.CharField(max_length=512)
	creditos = models.DecimalField(max_digits=2, decimal_places=0)
	tipo_aula = models.CharField(max_length=20)
	hteoria = models.BooleanField()
	hpractica = models.BooleanField()
	hlab = models.BooleanField()
	trime = models.CharField(max_length=8)
	ano = models.CharField(max_length=4)
	accion = models.CharField(max_length=20)
	afecta_carrera = models.CharField(max_length=35)
	trimestrep = models.BooleanField()
	requisito_cre = models.BooleanField()
	permiso_coord = models.BooleanField()
	tipo_materia = models.CharField(max_length=20)
	clase_materia = models.CharField(max_length=25)
	observaciones = models.CharField(max_length=512, blank=True, null=True)
	vigente = models.NullBooleanField()
	validadodace = models.BooleanField()
	especial = models.BooleanField()
	imparticion = models.CharField(max_length=15)
	usbidec = models.CharField(max_length=50, blank=True, null=True)
	obsanul = models.CharField(max_length=512, blank=True, null=True)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'solicitud'


class TipoAula(models.Model):
	nombre = models.CharField(primary_key=True, max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'tipo_aula'


class TipoMateria(models.Model):
	nombre = models.CharField(primary_key=True, max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'tipo_materia'


class TrimestreVigencia(models.Model):
	mes_inicio = models.IntegerField()
	mes_fin = models.IntegerField()
	nombre = models.CharField(primary_key=True, max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'trimestre_vigencia'


class Usuario(models.Model):
	usbid = models.CharField(primary_key=True, max_length=50)
	clave = models.CharField(max_length=16)
	nombre = models.CharField(max_length=60)
	email = models.CharField(max_length=50)
	tipo = models.CharField(max_length=50)

	class Meta:
		_DATABASE = 'gestionpae'
		managed = False
		db_table = 'usuario'
>>>>>>> 82b57394ac66cc61d44a2b2013fd930dd4fa5623
