from django.shortcuts import render
from rest_framework import serializers
from principal.models import *

class universal_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Universal
		fields = ('id','nombre','apellido','telefono','fecha_nacimiento','imagen_universi')