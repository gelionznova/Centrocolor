from distutils import extension
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields import CharField
from django.utils import timezone
from django.conf import settings
import os

#Tabla Universal

# def validarNumero(value):
#     if not solo_Digitos(value):
#         raise ValidationErr("este campo solo acepta numeros")



def upload_location(instance, filename):
    filebase, ext = filename.split(".")
    return "%s/%s.%s" %(instance.id,instance.documento,ext)

rol_usuario = (
	('estudiante', 'Estudiante'),
	('contratista', 'Contratista'),
    ('funcionario', 'Funcionario')
)  

tipo_rh = (
	('o  positivo (O+)', 'O positivo (O+)'),
	('o negativo (O-)', 'O negativo (O-)'),
    ('ab positivo (AB+)', 'AB positivo (AB+)'),
    ('ab negativo (AB-)', 'AB negativo (AB-)'),
    ('a positivo (A+)','A positivo (A+)'),
    ('a negativo (A-)','A negativo (A-)'),
    ('b positivo (B+)','B positivo (B+)'),
    ('b negativo (B-)','B negativo (B-)')   
)

opsiones_genero = (
    ('masculino', 'Masculino'),
    ('femenino', 'Femenino'),
)

class Universal(models.Model):
    nombre                    = models.CharField(max_length=75)
    apellido                  = models.CharField(max_length=75)   
    documento                 = models.CharField(max_length=12)   
    genero                    = models.CharField(max_length=12, choices=opsiones_genero, default= 'Masculino', blank=True, null=True)  
    tipo_de_rh                = models.CharField(max_length=200, choices=tipo_rh, default='O+')
    empresa_universidad       = models.CharField(max_length=75)
    rol_de_usuario            = models.CharField(max_length=200, choices=rol_usuario,default='estudiante')
    imagen_universi           = models.ImageField(upload_to=upload_location,null= True)
        
    def __unicode__(self):
        return self.nombre

class Empresa(models.Model):
    emrpesa           = models.CharField(max_length=75)
    nombres           = models.CharField(max_length=75)
    apellidos         = models.CharField(max_length=75)
    documento         = models.CharField(max_length=12)
    rh                = models.CharField(max_length=2)
    telefono          = models.CharField(max_length=12)    
    fecha_nacimiento  = models.DateField()
    imagen_empresa    = models.ImageField(upload_to="foto",null= True)
    
    def __str__(self):
        return self.empresa        



# fecha_nacimiento          = models.DateField()