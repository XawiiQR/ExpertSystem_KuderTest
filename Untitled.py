#!/usr/bin/env python3

def generar_codigo(fila):
	condiciones_si = []
	condiciones_no = []
	
	for i in range(3):
		if fila[i] == 'si':
			condiciones_si.append(f"fila[{i}] == 'si'")
		elif fila[i] == 'no':
			condiciones_no.append(f"fila[{i}] == 'no'")
			
	if fila.count('si') == 2:
		condiciones_no = condiciones_no[0]
		condiciones_si = " or ".join(condiciones_si)
		or_condiciones = f"{condiciones_no} and ({condiciones_si})"
		or_condiciones2 = f"{condiciones_no} or {condiciones_si}"
	elif fila.count('no') == 2:
		condiciones_si = condiciones_si[0]
		condiciones_no = " or ".join(condiciones_no)
		or_condiciones = f"{condiciones_si} and ({condiciones_no})"
		or_condiciones2 = f"{condiciones_si} or {condiciones_no}"
	else:
		or_condiciones = " or ".join(condiciones_si + condiciones_no)
		
	result = f"\tlambda fila: 2 if {or_condiciones} else 1 if {or_condiciones2} else 0"
	
	print(result)
	
while True:
	entrada = input("Introduce la fila en formato 'no si si' o 'salir' para terminar: ")
	if entrada.lower() == 'salir':
		break
	fila = entrada.split()
	if len(fila) == 3 and all(x in ['no', 'si'] for x in fila):
		generar_codigo(fila)
	else:
		print("Entrada inválida, por favor introduce una fila válida con tres valores 'no' o 'si'.")
		