import Conocimiento
import Reglas
import Percentiles
import Carreras

# Inicializar las puntuaciones
puntuaciones = {
    'AireLibre': 0, 'Mecanico': 0, 'Calculo': 0, 'Cientifico': 0,
    'Persuasivo': 0, 'Artistico': 0, 'Literario': 0, 'Musical': 0,
    'ServicioSocial': 0, 'Oficina': 0
}

def obtener_respuesta(opciones):
    respuestas = ['blanco', 'blanco', 'blanco']
    
    for i, opcion in enumerate(opciones):
        print(f"P{i+1}: {opcion}")
        
    for i, opcion in enumerate(opciones):
        print("\nEscoge una opción que te guste (si) y una que no te guste (no). La tercera será en blanco.\n")
        while True:
            respuesta = input(f"Para 'P{i+1}' : ").strip().lower()
            if respuesta in ['si', 'no', 'blanco']:
                if respuesta == 'si' and 'si' in respuestas:
                    print("Ya has escogido una opción que te gusta. Escoge otra respuesta.")
                elif respuesta == 'no' and 'no' in respuestas:
                    print("Ya has escogido una opción que no te gusta. Escoge otra respuesta.")
                else:
                    respuestas[i] = respuesta
                    break
            else:
                print("Debes contestar si, no o blanco.")
    return respuestas

def aplicar_regla(fila, reglas, area):
    for regla in reglas:
        puntuacion = regla(fila)
        area_base = ''.join(filter(str.isalpha, area))
        if area_base in puntuaciones:
            puntuaciones[area_base] += puntuacion
        else:
            print(f"Área desconocida: {area_base}")

def obtener_percentil(valor, escala):
    intervalos = Percentiles.intervalos_percentiles.get(escala, [])
    for intervalo in intervalos:
        if intervalo[0] <= valor <= intervalo[1]:
            return intervalo[2]
    return 0  # Retorna 0 si no se encuentra un percentil correspondiente

def motor_de_inferencia(hechos, base_de_conocimientos):
    for fila in hechos:
        area = fila[3]
        aplicar_regla(fila, base_de_conocimientos[area], area)

def mostrar_resultados():
    print("\nResultados del diagnóstico:")
    for area, puntuacion in puntuaciones.items():
        percentil = obtener_percentil(puntuacion, area)
        print(f"{area}: {puntuacion} puntos, Percentil: {percentil}")

def consulta():
    for area, opciones in Conocimiento.areas.items():
        if area in Conocimiento.preguntas_repetidas:
            pregunta_base = Conocimiento.preguntas_repetidas[area]
            if pregunta_base in Conocimiento.respuestas_repetidas:
                respuestas = Conocimiento.respuestas_repetidas[pregunta_base]
                Conocimiento.respuestas_areas[area] = respuestas
            else:
                print("Lee las siguientes preguntas y luego escoge\n")
                respuestas = obtener_respuesta(opciones)
                Conocimiento.respuestas_repetidas[pregunta_base] = respuestas
                Conocimiento.respuestas_areas[area] = respuestas
        else:
            print("Lee las siguientes preguntas y luego escoge\n")
            respuestas = obtener_respuesta(opciones)
            Conocimiento.respuestas_repetidas[area] = respuestas
            Conocimiento.respuestas_areas[area] = respuestas

        Conocimiento.respuestas_areas[area].append(area)
        Conocimiento.base_de_hechos.append(Conocimiento.respuestas_areas[area])

    for area, respuestas in Conocimiento.respuestas_areas.items():
        if area in Reglas.base_de_conocimientos:
            aplicar_regla(respuestas, Reglas.base_de_conocimientos[area], area)

    mostrar_resultados()
    sugerir_carreras()

def sugerir_carreras():
    limite = 70  # Este es el límite de percentil para considerar un área como relevante
    areas_relevantes = {area: obtener_percentil(puntuacion, area) for area, puntuacion in puntuaciones.items() if obtener_percentil(puntuacion, area) >= limite}
    
    if len(areas_relevantes) == 1:
        area = list(areas_relevantes.keys())[0]
        carreras = Carreras.Carreras[area]
        print(f"\nCarreras sugeridas para el área {area}:")
        for carrera in carreras:
            print(f"- {carrera}")
    elif len(areas_relevantes) >= 2:
        areas_ordenadas = sorted(areas_relevantes.items(), key=lambda x: x[1], reverse=True)
        if len(areas_ordenadas) > 2 and areas_ordenadas[1][1] == areas_ordenadas[2][1]:
            for area, percentil in areas_ordenadas:
                carreras = Carreras.Carreras[area]
                print(f"\nCarreras sugeridas para el área {area}:")
                for carrera in carreras:
                    print(f"- {carrera}")
        else:
            area1, area2 = areas_ordenadas[0][0], areas_ordenadas[1][0]
            combinacion = f"{area1}-{area2}"
            combinacion_inversa = f"{area2}-{area1}"
            if combinacion in Carreras.Carreras['Combinaciones']:
                carreras = Carreras.Carreras['Combinaciones'][combinacion]
                print(f"\nCarreras sugeridas para las áreas {area1} y {area2}:")
                for carrera in carreras:
                    print(f"- {carrera}")
            elif combinacion_inversa in Carreras.Carreras['Combinaciones']:
                carreras = Carreras.Carreras['Combinaciones'][combinacion_inversa]
                print(f"\nCarreras sugeridas para las áreas {area2} y {area1}:")
                for carrera in carreras:
                    print(f"- {carrera}")
            else:
                print(f"\nNo hay combinaciones definidas para las áreas {area1} y {area2}.")
    else:
        print("\nNo hay áreas que superen el límite especificado.")
        
        
if __name__ == "__main__":
    consulta()
    