
# Kuder Expert System

## Descripción

Este proyecto es un sistema experto basado en el Test de Kuder, diseñado para ayudar a los usuarios a identificar sus áreas de interés vocacional y recomendar carreras adecuadas. Utiliza una serie de preguntas y respuestas para evaluar las preferencias del usuario en diferentes áreas de conocimiento y devolver recomendaciones personalizadas.

## Características

- **Interfaz de usuario intuitiva**: Permite a los usuarios interactuar fácilmente con el sistema, respondiendo preguntas sobre sus intereses y preferencias.
- **Evaluación de múltiples áreas**: El sistema considera diversas áreas como:
  - Aire Libre
  - Mecánico
  - Científico
  - Persuasivo
  - Artístico
  - Literario
  - Musical
  - Servicio Social
  - Oficina
- **Reglas de decisión personalizadas**: Cada área de conocimiento tiene un conjunto de reglas específicas que determinan la puntuación y las recomendaciones basadas en las respuestas del usuario.
- **Sugerencias de carrera**: El sistema no solo evalúa las preferencias, sino que también sugiere carreras potenciales basadas en las puntuaciones obtenidas en diferentes áreas.
- **Registro de resultados**: Los resultados y recomendaciones se almacenan para que los usuarios puedan revisarlos más tarde.
- **Flexibilidad**: El sistema puede ser fácilmente modificado para incluir nuevas áreas de conocimiento o reglas de decisión.

## Tecnologías

- **Lenguaje**: Python
- **Estructuras de datos**: Utiliza diccionarios y listas para almacenar respuestas, puntuaciones y combinaciones de carreras.
- **Funciones Lambda**: Se implementan para simplificar la lógica de evaluación.
- **Sistema de Reglas**: Basado en lógica condicional para aplicar las reglas de decisión.

## Instalación

1. **Clona el repositorio**:
   ```
   git clone https://github.com/tu_usuario/kuder-expert-system.git
   ```
2. **Navega al directorio del proyecto**:
   ```
   cd kuder-expert-system
   ```
3. **Instala Python**: Asegúrate de tener Python (versión 3.6 o superior) instalado en tu máquina.
4. **(Opcional) Crea un entorno virtual**: Es recomendable crear un entorno virtual para gestionar las dependencias:
   ```
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate  # En Windows
   ```

## Uso

Ejecuta el sistema experto de Kuder con el siguiente comando:
```
python main.py
```
Sigue las instrucciones en pantalla para responder las preguntas y recibir recomendaciones vocacionales. Asegúrate de proporcionar respuestas precisas para obtener las mejores recomendaciones.

## Ejemplo de Uso

Al iniciar el sistema, verás un conjunto de preguntas que podrás responder con "sí" o "no". Basado en tus respuestas, el sistema calculará tus puntuaciones en diferentes áreas y te sugerirá carreras que se alineen con tus intereses.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar con el proyecto, por favor sigue estos pasos:

1. **Haz un fork del repositorio**.
2. **Crea una nueva rama**:
   ```
   git checkout -b feature/nueva-caracteristica
   ```
3. **Realiza tus cambios y haz commit**:
   ```
   git commit -m 'Añadir nueva característica'
   ```
4. **Haz push a la rama**:
   ```
   git push origin feature/nueva-caracteristica
   ```
5. **Abre un Pull Request** en GitHub para que podamos revisar tus cambios.

## Autor
- Javier Wilber Quispe Rojas

```
