#!/usr/bin/env python3

# Diccionario de intervalos y percentiles para cada escala vocacional
intervalos_percentiles = {
	'AireLibre': [
		(1, 19, 5), (20, 25, 10), (26, 29, 15), (30, 31, 20), (31, 34, 25),
		(35, 36, 30), (37, 38, 35), (39, 49, 40), (41, 42, 45), (43, 45, 50),
		(46, 46, 55), (47, 48, 60), (49, 51, 65), (52, 54, 75), (55, 57, 80),
		(58, 60, 85), (61, 64, 90), (65, 69, 95), (70, 100, 100)
	],
	# Agrega aquí los intervalos para las demás escalas
	'Mecanico': [
		(1, 22, 5), (23, 26, 10), (27, 29, 15), (30, 31, 20), (31, 34, 25), (35, 37, 35), (38, 38, 40), (39, 42, 45), (43, 43, 50), (44, 45, 65),  (46, 46, 70),(47, 47, 75), (48, 49, 80),
		(50, 52, 85), (53, 54, 90), (55, 58, 95), (59, 100, 100)
	],
	'Calculo': [
		(1, 13, 5), (14, 16, 10), (17, 19, 15), (20, 21, 20),(22,22, 25), (23, 25, 35), (26, 28, 45),(29, 29, 55), (31, 31, 60), (32, 32, 65),(34,34,70), (35, 35, 75), (36, 36, 80),(37, 38, 85), (39, 40, 90), (41, 44, 95), (45, 100, 100)
		# Ejemplo: (1, 10, 5), (11, 20, 10), ... debes ajustar según la tabla
	],
	'Cientifico': [
		(1, 26, 5), (27, 31, 10), (32, 34, 15), (35, 36, 20), (37, 37, 25),(38, 40, 30), (41, 41, 35), (42, 43, 40), (44, 44, 45), (46, 46, 50),(47, 47, 55), (48, 49, 60), (50, 50, 65),(51,52,70),(53, 53, 75), (54, 55, 80),(56, 58, 85), (59, 59, 90), (60, 65, 95), (66, 100, 100)
		# Ejemplo: (1, 10, 5), (11, 20, 10), ... debes ajustar según la tabla
	],
	'Persuasivo': [
		(1, 18, 5), (19, 22, 10), (23, 24, 15), (25, 26, 20), (27, 29, 25), (30, 32, 35),(33, 33, 45), (34, 35, 50),(36, 36, 55), (37, 38, 60), (39, 39, 65),(40,41,70),(42, 44, 80),(45, 45, 85), (46, 49, 90), (50, 52, 95), (53, 100, 100)
		# Ejemplo: (1, 10, 5), (11, 20, 10), ... debes ajustar según la tabla
	],
	'Artistico': [
		(1, 10, 5), (11, 13, 10), (14, 16, 15),(17, 19, 25),(20, 22, 35),(23, 23, 45), (24, 25, 50),(26, 28, 60),(29,30,70), (31, 31, 75), (32, 33, 80),
		(34, 35, 85), (36, 36, 90), (37, 40, 95), (41, 100, 100)
		# Ejemplo: (1, 10, 5), (11, 20, 10), ... debes ajustar según la tabla
	],
	'Literario': [
		(1, 6, 5), (7, 9, 10), (10, 11, 15), (12, 14, 20), (15, 15, 35), (17, 17, 40), (18, 18, 45), (20, 20, 50),(21, 21, 65),(22,23,70), (24, 25, 80),
		(26, 26, 85), (27, 28, 90), (29, 31, 95), (32, 100, 100)
		# Ejemplo: (1, 10, 5), (11, 20, 10), ... debes ajustar según la tabla
	],
	'Musical': [
		(1, 1, 5),(2, 4, 15), (6, 6, 20), (7, 7, 25),
		(8, 9, 35), (10, 10, 50),(11, 11, 65),(12,12,70), (13, 13, 80),
		(14, 15, 85), (16, 22, 95), (23, 100, 100)
		# Ejemplo: (1, 10, 5), (11, 20, 10), ... debes ajustar según la tabla
	],
	'ServicioSocial': [
		(1, 22, 5), (23, 25, 10), (26, 28, 15), (29, 31, 20), (32, 32, 25),  (33, 35, 40), (36, 39, 45), (43, 41, 50),
		(46, 43, 55), (44, 44, 60), (45, 46, 65),(47,47,70), (48,50, 75), (51, 52, 80),
		(53, 54, 85), (55, 58, 90), (59, 61, 95), (62, 100, 100)
		# Ejemplo: (1, 10, 5), (11, 20, 10), ... debes ajustar según la tabla
	],
	'Oficina': [
		(1, 23, 5), (24, 29, 10), (30, 32, 15), (33, 35, 20), (36, 36, 25),
		(37, 39, 30), (40, 41, 35), (42, 42, 40),(43,44,45), (45, 47, 50),
		(46, 48, 55), (59, 50, 60), (51, 51, 65),(52,53,70), (54,56, 75), (57, 59, 80),
		(60, 60, 85), (61, 65, 90), (66, 69, 95), (70, 100, 100)
		# Ejemplo: (1, 10, 5), (11, 20, 10), ... debes ajustar según la tabla
	],
}
