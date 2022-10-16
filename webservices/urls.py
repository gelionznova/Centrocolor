from django.urls import path, include
from rest_framework import routers
from principal.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'universal', universal_viewset)


urlpatterns = [
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]