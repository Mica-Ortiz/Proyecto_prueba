from django.shortcuts import render

def inicio(request):
    return render(request, "AppUNR/index.html")

def cursos(request):
    return render(request, "AppUNR/cursos.html")

def profesores(request):
    return render(request, "AppUNR/profesores.html")

def estudiantes(request):
    return render(request, "AppUNR/estudiantes.html")

def entregables(request):
    return render(request, "AppUNR/entregables.html")
