from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns =[
   # path('formulario', views.formulario, name="Formulario"),
   path('contacto', views.contacto, name="Contacto"),
   path('registrarAlumno/', views.FormularioUniversalView.index, name='registrarAlumno'),
    path('guardarAlumno/', views.FormularioUniversalView.procesar_formulario, name='guardarAlumno'),   
]