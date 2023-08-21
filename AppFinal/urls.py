from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from AppADM import views2
from AppFinal import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sector', views.sector, name='sector'),
    path('empleado', views.empleado, name='empleado'),
    path('cliente', views.cliente, name='cliente'),
    path('encargado', views.encargado, name='encargado'),
    path('pagina404', views.pagina404, name='pagina404'),
    #path('SectorForm', views.sectorForm, name= 'sectorForm'),
    #path('EmpleadoForm', views.empleadoForm, name= 'EmpleadoForm'),
    #path('ClienteForm', views.clienteForm, name= 'ClienteFom'),
    #path('EncargadoForm/', views.encargadoForm, name= 'EncargadoForm'),
    path('buscarCliente', views.buscarCliente, name= 'buscarCliente'),
    path('buscar/', views.buscar, name= 'buscar'),
    path('verClientes', views.verClientes, name= 'verClientes'),
    path('eliminarCliente/<nombre_cliente>', views.eliminarCliente, name='eliminarCliente'),
    path('editarCliente/<nombre_cliente>', views.editarCliente, name='editarCliente'),
    
    path('verEmpleado', views.verEmpleado, name= 'verEmpleado'),
    path('eliminarEmpleado/<nombre_empleado>', views.eliminarEmpleado, name='eliminarEmpleado'),
    path('editarEmpleado/<nombre_empleado>', views.editarEmpleado, name='editarEmpleado'),
    
    path('AppADM/login', views2.login_request, name='login'),
    path('AppADM/registro', views2.register, name='Registro'),
    path('AppADM/logout', LogoutView.as_view(template_name='AppADM/logout.html'), name='Logout'),
    
    path('AppADM/editarPerfil', views2.editarPerfil, name='editarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='agregarAvatar')
    

]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

