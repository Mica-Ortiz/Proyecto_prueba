from datetime import datetime as dt

from django.http import HttpResponse

from django.template import Template, Context, loader

def saludo(request):
	dia = dt.now()
	texto = f"Hola Django <br> Coder <br> {dia}"
	return HttpResponse(texto)

def mi_nombre(request, nombre):
	texto = f"Mi nombre es {nombre}"
	return HttpResponse(texto)

def probandotemplate (self):

	nom = "Micaela"
	ape = "Ortiz"
	lista_de_idiotas = ["F","E","N"]

	diccionario = {"nombre": nom, "apellido": ape, "lista":lista_de_idiotas} #lo vamos a enviar al contexto
	


	#mihtml = open("C:/Users/jj6385/OneDrive/Proyecto_1/Proyecto_final/Proyecto_prueba/Proyecto_prueba/plantillas/index.html")

	#plantilla = Template(mihtml.read())
	
	#mihtml.close()

	#micontexto = Context (diccionario) #le enviamos el diccionario al contexto

	plantilla = loader.get_template('index.html')

	documento = plantilla.render(diccionario)

	return HttpResponse(documento)

