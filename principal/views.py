from importlib.resources import path
from os import rename
import os
import pathlib
from pickle import NONE
from tkinter import image_names
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . forms import *

# Primera vista

def inicio(request):

    return render(request,"inicio.html")

def formulario(request):

    return render(request,"formulario.html")

def contacto(request):

    return render(request,"contacto.html")

# VISTA UNIVERSITARIO
class FormularioUniversalView(HttpRequest):

	def index(request):
		universi = FormularioUniversal()
		return render(request, "formulario.html", {"form":universi})						

	def procesar_formulario(request):
		universi = FormularioUniversal(request.POST, request.FILES or NONE)
		if universi.is_valid():
			universi.save()
			universi = FormularioUniversal()
		return render(request, "inicio.html", {"form":universi, "mensaje": 'OK'})

		

	

	
