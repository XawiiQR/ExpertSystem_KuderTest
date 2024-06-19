#!/usr/bin/env python3

# Base de conocimientos: diccionario de reglas específicas para cada opción
base_de_conocimientos = {
	#Fila1
	'AireLibre011': [
		lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0

	],
	'Calculo012': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'no' else 0
	],

	'Persuasivo012': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'ServicioSocial012': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],


	'AireLibre013': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,

	],
	'AireLibre014': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,

	],
	'AireLibre015': [
		lambda fila: 0 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 0 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

	'AireLibre016': [
		lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

	'AireLibre018': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0
	],
	'Cientifico017': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Persuasivo018': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Musical018': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina019': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Mecanico010': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico010': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Persuasivo010': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],


	#Fila2

	'Mecanico021': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Mecanico022': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Artistico022': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Artistico023': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,

	],
	'Mecanico024': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,

	],
  'Artistico024': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,

	],

  'Musical024': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,

	],

	'AireLibre025': [
		lambda fila: 2 if fila[1] == 'no' and (fila[0] == 'si' or fila[2] == 'si') else 1 if fila[1] == 'no' or fila[0] == 'si' or fila[2] == 'si' else 0,
	],

	'AireLibre026': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'AireLibre027': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Persuasivo027': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'AireLibre028': [
		lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

	'AireLibre029': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'AireLibre020': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Oficina020': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

  'Cientifico020': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0
	],

	#Fila3

	'ServicioSocial031': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'ServicioSocial032': [
		lambda fila: 0 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 0 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo033': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'ServicioSocial033': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina034': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Persuasivo035': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],


	'Artistico035': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Cientifico036': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Artistico036': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico037': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
		],

	'Musical037': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina037': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico038': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Musical038': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],


	'Persuasivo039': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina039': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'AireLibre030': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

 #Fila de Javi ##################################################################################################################################################################
	#Fila4

	'AireLibre041': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'AireLibre042': [
		 lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

	'AireLibre043': [
		lambda fila: 2 if fila[1] == 'no' and (fila[0] == 'si' or fila[2] == 'si') else 1 if fila[1] == 'no' or fila[0] == 'si' or fila[2] == 'si' else 0,
	],

	'Científico044': [
		lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

	'Literario044': [
		lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

	'ServicioSocial044': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico045': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'ServicioSocial046': [
		 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina046': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Cientifico047': [
		lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],
	'ServicioSocial047': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Oficina047': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico048': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'ServicioSocial048': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico049': [
		 lambda fila: 0 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 0 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico040': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'ServicioSocial040': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina040': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],





#Fila5

	'Cientifico051': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Musical051': [
		  lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico052': [
		 lambda fila: 2 if fila[2] == 'no' and (fila[0] == 'si' or fila[1] == 'si') else 1 if fila[2] == 'no' or fila[0] == 'si' or fila[1] == 'si' else 0,
	],

	'Oficina052': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Persuasivo053': [
		 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'AireLibre054': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo055': [
		  lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Literario055': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Oficina055': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Literario056': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina056': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Literario057': [
		  lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'AireLibre058': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Persuasivo058': [
		  lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Oficina058': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico059': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Literario059': [
		 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'ServicioSocial059': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'ServicioSocial050': [
		 lambda fila: 0 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 0 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],




#Fila6

	'Cientifico061': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo061': [
		 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'ServicioSocial061': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina061': [
		 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Persuasivo062': [
		  lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Oficina062': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'AireLibre063': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Persuasivo063': [
		  lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Artistico063': [
		 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico064': [
		  lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Artistico064': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'ServicioSocial064': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico065': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Oficina065': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Mecanico066': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico066': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Artistico066': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Calculo067': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Persuasivo067': [
		  lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Calculo068': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo068': [
		  lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'ServicioSocial068': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Calculo069': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Literario069': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'ServicioSocial069': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina069': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'AireLibre060': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Persuasivo060': [
		  lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'ServicioSocial060': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],





#Fila7


	'AireLibre071': [
		lambda fila: 0 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 0 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

	'AireLibre072': [
		 lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

	'Cientifico072': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo072': [
		 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico073': [
		 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo073': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina074': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico075': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Musical075': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Mecanico076': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Persuasivo076': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Musical076': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'ServicioSocial076': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico077': [
	 	lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo077': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Artistico077': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Mecanico078': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Cientifico078': [
		  lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina078': [
		 lambda fila: 2 if fila[1] == 'no' and (fila[0] == 'si' or fila[2] == 'si') else 1 if fila[1] == 'no' or fila[0] == 'si' or fila[2] == 'si' else 0,
	],

	'Cientifico079': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'ServicioSocial079': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Mecanico070': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],




#Fila8

	'Literario081': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina081': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Oficina082': [
		 lambda fila: 0 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 0 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Calculo083': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Persuasivo083': [
		 lambda fila: 2 if fila[1] == 'no' and (fila[0] == 'si' or fila[2] == 'si') else 1 if fila[1] == 'no' or fila[0] == 'si' or fila[2] == 'si' else 0,
	],

	'AireLibre084': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'AireLibre085': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico085': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'AireLibre086': [
		 lambda fila: 2 if fila[2] == 'no' and (fila[0] == 'si' or fila[1] == 'si') else 1 if fila[2] == 'no' or fila[0] == 'si' or fila[1] == 'si' else 0,
	],

	'Cientifico086': [
		 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Cientifico087': [
		 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Literario087': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Mecanico088': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Calculo088': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo088': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina088': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Mecanico089': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo089': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Musical089': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'ServicioSocial089': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Mecanico080': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Calculo080': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Persuasivo080': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],


 #Fila de Javi ##################################################################################################################################################################

	#Fila9

	'ServicioSocial091': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Oficina091': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
		],
	'Mecanico092': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina092': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
		],
	'Mecanico093': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Musical093': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
		],
	'ServicioSocial093': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Mecanico094': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'AireLibre095': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina095': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
		],
 'ServicioSocial095': [
			lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'AireLibre096': [
			 lambda fila: 2 if fila[2] == 'no' and (fila[0] == 'si' or fila[1] == 'si') else 1 if fila[2] == 'no' or fila[0] == 'si' or fila[1] == 'si' else 0
	],

	'Persuasiv0097': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'ServicioSocial097': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina097': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
		],
	'AireLibre098': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Oficina099': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo090': [
			 lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],
	'Artistico090': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
		],

	'Literario090': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
			],

#Fila10

	'Cientifico101': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Artistico101': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Literario101': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
		],
	'Mecanico102': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Calculo102': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
		],
	'Oficina103': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina104': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Mecanico105': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Persuasivo105': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Artístico105': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
		],

	'Mecánico106': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
		],

	'ServicioSocial107': [
			 lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

	'Mecanico108': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Artistico108': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico108': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Calculo109': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico109': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'ServicioSocial109': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina109': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo100': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina100': [
			 lambda fila: 2 if fila[1] == 'no' and (fila[0] == 'si' or fila[2] == 'si') else 1 if fila[1] == 'no' or fila[0] == 'si' or fila[2] == 'si' else 0,
	],

 #Fila11

	'Calculo111': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Musical111': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Persuasivo111': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo112': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina112': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Persuasivo113': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Persuasivo114': [
			 lambda fila: 0 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 0 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'AireLibre115': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Calculo116': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Artistico116': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Mecanico117': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Calculo117': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Calculo118': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Artistico118': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Mecanico119': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Calculo119': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Calculo110': [
			 lambda fila: 0 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 0 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],


	#Fila12

	'Artistico121': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Mecanico122': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Oficina123': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,

	],
	'Persuasivo124': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Literario124': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Persuasivo125': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'ServicioSocial125': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Literario125': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Persuasivo126': [
			 lambda fila: 0 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 0 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,

	],

	'Artistico128': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Literario128': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'ServicioSocial128': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
		],
	'Artistico129': [
			 lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,

	],
	'Literario129': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Oficina129': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,

	],
	'Oficina120': [
			 lambda fila: 0 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 0 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,

	],


 #Fila13

	'Mecanico131': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],

	'Calculo131': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Oficina131': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],

	'Calculo132': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Artistico132': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
		],

	'Mecanico133': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Calculo133': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Oficina133': [
			 lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],
	'Mecanico134': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
	'Calculo134': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Mecanico135': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico135': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
		],
	'Artistico135': [
			 lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
		],

	'AireLibre136': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
	'Cientifico136': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
		],
	'Musical136': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
		],

	'Persuasivo138': [
			 lambda fila: 2 if fila[1] == 'no' and (fila[0] == 'si' or fila[2] == 'si') else 1 if fila[1] == 'no' or fila[0] == 'si' or fila[2] == 'si' else 0,
	],

	'Calculo139': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
	'Persuasivo139': [
			 lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],

	'Literario130': [
			 lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0
	],
	'Oficina130': [
			 lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],

##################################################################################################################################################################
#Jharold
#Fila 14
    'AireLibre141': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Artistico142': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Literario142': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'AireLibre143': [
		lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],
    'AireLibre144': [
		lambda fila: 0 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 0 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Mecanico145': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'ServicioSocial146': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Mecanico146': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Oficina146': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Calculo147': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Mecanico147': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Oficina148': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Musical149': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'ServicioSocial149': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Mecanico140': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'ServicioSocial140': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],


	#Fila 15
    'AireLibre151': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
    ],
    'AireLibre152': [
        lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'AireLibre153': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Persuasivo153': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'AireLibre154': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Persuasivo154': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Literario154': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'AireLibre155': [
		lambda fila: 0 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 0 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Calculo156': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Oficina156': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'AireLibre157': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Artistico157': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Literario157': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'AireLibre158': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'ServicioSocial158': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'AireLibre159': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Oficina159': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Musical159': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Mecanico150': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Calculo150': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Oficina150': [
		lambda fila: 2 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 1 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],


	#Fila 16
    'Oficina161': [
		lambda fila: 0 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 0 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],
    'Mecanico162': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'ServicioSocial162': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Oficina162': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Mecanico163': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Oficina164': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Oficina165': [
		lambda fila: 2 if fila[2] == 'no' and (fila[0] == 'si' or fila[1] == 'si') else 1 if fila[2] == 'no' or fila[0] == 'si' or fila[1] == 'si' else 0,
	],
    'Persuasivo165': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'AireLibre166': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Persuasivo167': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Oficina167': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Oficina168': [
		lambda fila: 0 if fila[0] == 'no' and (fila[1] == 'si' or fila[2] == 'si') else 0 if fila[0] == 'no' or fila[1] == 'si' or fila[2] == 'si' else 0,
	],
    'Oficina169': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Persuasivo160': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Artistico160': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Literario160': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Oficina160': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],


	#Fila 17
	  'AireLibre171': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Calculo171': [
		lambda fila: 2 if fila[1] == 'no' and (fila[0] == 'si' or fila[2] == 'si') else 1 if fila[1] == 'no' or fila[0] == 'si' or fila[2] == 'si' else 0,
	],
    'Oficina171': [
		lambda fila: 2 if fila[1] == 'no' and (fila[0] == 'si' or fila[2] == 'si') else 1 if fila[1] == 'no' or fila[0] == 'si' or fila[2] == 'si' else 0,
	],
    'Oficina172': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Artistico173': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'ServicioSocial173': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Calculo174': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Mecanico174': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Artistico175': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Musical175': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Oficina176': [
		lambda fila: 0 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 0 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Cientifico177': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],
    'Artistico177': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Mecanico177': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'ServicioSocial178': [
		lambda fila: 2 if fila[1] == 'si' and (fila[0] == 'no' or fila[2] == 'no') else 1 if fila[1] == 'si' or fila[0] == 'no' or fila[2] == 'no' else 0,
	],
    'Mecanico178': [
		lambda fila: 2 if fila[0] == 'si' and (fila[1] == 'no' or fila[2] == 'no') else 1 if fila[0] == 'si' or fila[1] == 'no' or fila[2] == 'no' else 0,
	],
    'Oficina178': [
		lambda fila: 2 if fila[2] == 'si' and (fila[0] == 'no' or fila[1] == 'no') else 1 if fila[2] == 'si' or fila[0] == 'no' or fila[1] == 'no' else 0,
	],


}
