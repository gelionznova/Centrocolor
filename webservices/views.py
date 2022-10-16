from principal.models import *
from .serializer import *
from rest_framework import viewsets

# API USUARIO
class universal_viewset(viewsets.ModelViewSet):
	queryset = Universal.objects.all()
	serializer_class = universal_serializer