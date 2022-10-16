from . models import Empresa, Universal
from django import forms


#Formulario para cargar archivos



class FormularioUniversal(forms.ModelForm):
	nombre                    = forms.CharField(max_length=75, label="Nombres")
	apellido                  = forms.CharField(max_length=75, label="Apellidos")
	documento                 = forms.CharField(max_length=12, label="Documento de identidad")
		
	class Meta:
		model = Universal
		fields = ['nombre','apellido','documento','genero','tipo_de_rh','empresa_universidad','rol_de_usuario','imagen_universi']

class FormularioEmpresa(forms.ModelForm):
	class Meta:
		model = Empresa
		fields = '__all__'
		widgets ={'fecha_nacimiento': forms.DateInput(attrs={'type':'date'})}		
