from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmpleadoForm(forms.Form):
    nombre_empleado = forms.CharField()
    apellido_empleado = forms.CharField()
    email = forms.EmailField()
    
class ClienteForm(forms.Form):
    nombre_cliente = forms.CharField()
    apellido_cliente = forms.CharField()
    email = forms.EmailField()
    
class SectorForm(forms.Form):
    nombre_empleado = forms.CharField()
    zona_trabajo = forms.CharField()
    
    
class EncargadoForm(forms.Form):
    nombre_encargado = forms.CharField()
    apellido_encargado = forms.CharField()
    email = forms.EmailField()
    sector = forms.CharField()
    

class AvatarFormulario(forms.Form):
    #especificar los campos
    username=forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['imagen']
        help_texts = {k:"" for k in fields}