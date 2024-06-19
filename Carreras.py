#!/usr/bin/env python3

Carreras = {
	'AireLibre': [
		'Ingeniería Ambiental',
		'Ingeniería Geofísica',
		'Ingeniería Geológica',
		'Ingeniería de Minas',
		'Agronomía',
		'Ingeniería Pesquera'
	],
	'Mecanico': [
		'Ingeniería Química',
		'Ingeniería de Materiales',
		'Ingeniería Metalúrgica',
		'Ingeniería de Industrias Alimentarias',
		'Ingeniería de Sistemas',
		'Ingeniería Eléctrica',
		'Ingeniería Electrónica',
		'Ingeniería Mecánica',
		'Ingeniería Industrial',
		'Ingeniería de Telecomunicaciones'
	],
	'Calculo': [
		'Ciencia de la Computación',
		'Matemáticas',
		'Economía',
		'Contabilidad',
		'Finanzas'
	],
	'Cientifico': [
		'Ingeniería Química',
		'Ingeniería Eléctrica',
		'Ingeniería Electrónica',
		'Ingeniería de Sistemas',
		'Ingeniería Geofísica',
		'Ingeniería Geológica',
		'Física',
		'Química',
		'Biología',
		'Ciencias de la Nutrición',
		'Ingeniería Pesquera',
		'Medicina',
		'Ingeniería de Materiales'
	],
	'Persuasivo': [
		'Derecho',
		'Relaciones Industriales',
		'Ciencias de la Comunicación Esp. Periodismo',
		'Ciencias de la Comunicación Esp. Relaciones Públicas',
		'Marketing',
		'Administración',
		'Gestión Pública',
		'Gestión de Empresas',
		'Gestión de Proyectos'
	],
	'Artistico': [
		'Arquitectura',
		'Artes Especialidad de Plásticas',
		'Artes Especialidad de Música'
	],
	'Literario': [
		'Filosofía',
		'Literatura y Lingüística',
		'Ciencias de la Comunicación Esp. Periodismo',
		'Ciencias de la Comunicación Esp. Relaciones Públicas',
		'Historia'
	],
	'Musical': [
		'Artes Especialidad de Música'
	],
	'ServicioSocial': [
		'Enfermería',
		'Trabajo Social',
		'Antropología',
		'Sociología',
		'Turismo y Hotelería',
		'Esp. Ciencias Naturales',
		'Esp. Ciencias Sociales',
		'Esp. Educación Física',
		'Esp. Educación Inicial',
		'Esp. Educación Primaria',
		'Esp. Físico Matemática',
		'Esp. Lengua, literatura, filosofía y psicología',
		'Esp. Idiomas (inglés-francés)'
	],
	'Oficina': [
		'Contabilidad',
		'Finanzas',
		'Administración',
		'Banca y Seguros',
		'Gestión Pública',
		'Gestión de Empresas',
		'Gestión de Proyectos'
	],
	'Combinaciones': {
		'AireLibre-Mecanico': [
			'Ingeniería Ambiental',
			'Ingeniería Geofísica',
			'Ingeniería Geológica',
			'Ingeniería de Minas',
			'Agronomía',
			'Ingeniería Pesquera'
		],
		'AireLibre-Calculo': [
			'Ingeniería Ambiental'
		],
		'AireLibre-Cientifico': [
			'Ingeniería Geofísica',
			'Ingeniería Geológica',
			'Ingeniería de Minas',
			'Agronomía',
			'Ingeniería Pesquera'
		],
		'AireLibre-ServicioSocial': [
			'Ingeniería Ambiental',
			'Ingeniería Pesquera'
		],
		'Mecanico-Calculo': [
			'Ingeniería de Sistemas',
			'Ingeniería Eléctrica',
			'Ingeniería Electrónica',
			'Ingeniería Mecánica',
			'Ingeniería Industrial',
			'Ingeniería de Telecomunicaciones'
		],
		'Mecanico-Cientifico': [
			'Ingeniería Química',
			'Ingeniería Eléctrica',
			'Ingeniería Electrónica',
			'Ingeniería de Sistemas',
			'Ingeniería Geofísica',
			'Ingeniería Geológica',
			'Física',
			'Química',
			'Biología',
			'Ingeniería de Materiales'
		],
		'Mecanico-Persuasivo': [
			'Ingeniería Industrial'
		],
		'Mecanico-Artistico': [
			'Arquitectura'
		],
		'Mecanico-Musical': [
			'Ingeniería de sonido'
		],
		'Mecanico-ServicioSocial': [
			'Ingeniería Industrial'
		],
		'Calculo-Cientifico': [
			'Ingeniería de Sistemas',
			'Ingeniería Eléctrica',
			'Ingeniería Electrónica',
			'Física',
			'Química',
			'Matemáticas',
			'Ciencia de la Computación'
		],
		'Calculo-Persuasivo': [
			'Economía'
		],
		'Calculo-Artistico': [
			'Arquitectura'
		],
		'Calculo-ServicioSocial': [
			'Economía'
		],
		'Calculo-Oficina': [
			'Contabilidad',
			'Finanzas'
		],
		'Cientifico-Persuasivo': [
			'Ingeniería Industrial',
			'Relaciones Industriales'
		],
		'Cientifico-Artistico': [
			'Arquitectura'
		],
		'Cientifico-Literario': [
			'Medicina',
			'Biología',
			'Química',
			'Filosofía',
			'Literatura y Lingüística'
		],
		'Cientifico-Musical': [
			'Ingeniería de sonido'
		],
		'Cientifico-ServicioSocial': [
			'Medicina',
			'Enfermería',
			'Trabajo Social',
			'Antropología',
			'Sociología'
		],
		'Persuasivo-Artistico': [
			'Arquitectura',
			'Artes Especialidad de Plásticas'
		],
		'Persuasivo-Literario': [
			'Derecho',
			'Ciencias de la Comunicación Esp. Periodismo',
			'Ciencias de la Comunicación Esp. Relaciones Públicas',
			'Historia'
		],
		'Persuasivo-Musical': [
			'Artes Especialidad de Música'
		],
		'Persuasivo-ServicioSocial': [
			'Derecho',
			'Relaciones Industriales',
			'Trabajo Social',
			'Antropología',
			'Sociología'
		],
		'Artistico-Literario': [
			'Artes Especialidad de Plásticas',
			'Literatura y Lingüística'
		],
		'Artistico-ServicioSocial': [
			'Artes Especialidad de Plásticas'
		],
		'Literario-Musical': [
			'Artes Especialidad de Música',
			'Literatura y Lingüística'
		],
		'Literario-ServicioSocial': [
			'Filosofía',
			'Literatura y Lingüística',
			'Ciencias de la Comunicación Esp. Periodismo',
			'Ciencias de la Comunicación Esp. Relaciones Públicas'
		],
		'Musical-ServicioSocial': [
			'Artes Especialidad de Música'
		],
		'ServicioSocial-Oficina': [
			'Contabilidad',
			'Finanzas',
			'Administración',
			'Banca y Seguros',
			'Gestión Pública',
			'Gestión de Empresas',
			'Gestión de Proyectos'
		]
	}
}
