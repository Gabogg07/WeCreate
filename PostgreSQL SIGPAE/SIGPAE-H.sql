\c gestionpae;

CREATE TABLE Document (
	id			SERIAL NOT NULL,
	codigo		VARCHAR(10) NOT NULL,
	periodo		VARCHAR(10),
	anio		INTEGER,
	nombre		VARCHAR(512) NOT NULL,
	docfile		VARCHAR(2048) NOT NULL,
	CONSTRAINT PK_DOCUMENT PRIMARY KEY(id)
);

CREATE TABLE Historial (
	dependencia 			VARCHAR(512),
	decanato 				VARCHAR(512),
	coordinacion_D1 		VARCHAR(512),
	coordinacion_D2 		VARCHAR(512),
	coordinacion_D3			VARCHAR(512),
	division				VARCHAR(512),
	departamento_D1			VARCHAR(512),
	departamento_D2			VARCHAR(512),
	departamento_D3			VARCHAR(512),
	departamento_D4			VARCHAR(512),
	codigo_asignatura		VARCHAR(512),
	denominacion			VARCHAR(512),
	periodo					VARCHAR(512),
	anio 					INTEGER,
	horas_T 				INTEGER,
	horas_P 				INTEGER,
	horas_L 				INTEGER,
	num_creditos			INTEGER,
	requisitos				VARCHAR(512),
	estrategias_met			VARCHAR(512),
	estrategias_ev			VARCHAR(512),
	contenido				VARCHAR(512),
	objetivos_generales		VARCHAR(512),
	objetivos_especificos	VARCHAR(512),
	fuentes_info			VARCHAR(512),
	docfile_id 				SERIAL PRIMARY KEY
							CONSTRAINT fk_document
							REFERENCES Document(id)
							ON DELETE CASCADE
							ON UPDATE CASCADE
);

CREATE TABLE Transcripcion (
	dependencia 			VARCHAR(512),
	decanato 				VARCHAR(512),
	coordinacion_D1 		VARCHAR(512),
	coordinacion_D2 		VARCHAR(512),
	coordinacion_D3			VARCHAR(512),
	division				VARCHAR(512),
	departamento_D1			VARCHAR(512),
	departamento_D2			VARCHAR(512),
	departamento_D3			VARCHAR(512),
	departamento_D4			VARCHAR(512),
	codigo_asignatura		VARCHAR(512),
	denominacion			VARCHAR(512),
	periodo					VARCHAR(512),
	anio 					INTEGER,
	horas_T 				INTEGER,
	horas_P 				INTEGER,
	horas_L 				INTEGER,
	num_creditos			INTEGER,
	requisitos				VARCHAR(512),
	estrategias_met			VARCHAR(512),
	estrategias_ev			VARCHAR(512),
	contenido				VARCHAR(512),
	objetivos_generales		VARCHAR(512),
	objetivos_especificos	VARCHAR(512),
	fuentes_info			VARCHAR(512),
	docfile_id 				SERIAL PRIMARY KEY
							CONSTRAINT fk_document
							REFERENCES Document(id)
							ON DELETE CASCADE
							ON UPDATE CASCADE
);