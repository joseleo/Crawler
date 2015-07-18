# Crawler
Spider para la descarga de posts de la página principal de OSL.
Por cada post que aparece en la página principal de osl.ugr.es de debe obtener:

- titulo
- autor
- contenido
- lista de categorías
- lista de etiquetas

Los datos se almacenan en XML, y si alguna entrada no tiene asignada ninguna etiqueta: se almacenan los datos correspondientes
en otro fichero distinto.