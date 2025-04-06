# Ejercicio de Feedback 1 - Áreas de aplicación y casos de uso: entornos con datos no estructurados

Autor: Néstor Ojeda González

Este es el entregable del primer ejercicio de feedback. Consta de las siguientes partes:

- code : contiene el código de la aplicación de una pequeña interfaz de usuario que implementa el ejercicio.
- docs : contiene unos textos de ejemplo para probar la aplicación.
- notebook: contiene un Jupyter Notebook que implementa tambien el ejercicio.

## Instrucciones para ejecutar la interfaz de usuario

Para ejecutar este proyecto, instala las dependencias:

```bash
pip install -r requirements.txt
streamlit run ./code/ui.py
```
Luego, abre tu navegador web y navega a `http://localhost:8501` para acceder a la aplicación.

## Uso
1. Sube un documento de texto en español.
2. La aplicación procesará el documento y proporcionará:
    - Un resumen del texto
    - Resultados del análisis de sentimientos
    - Texto traducido al inglés

La versión completa la he subido a mi repositorio de GitHub, donde puedes encontrar el código fuente y la documentación adicional. Puedes acceder al repositorio en el siguiente [enlace](https://github.com/nestorojeda/SenseTranslate)