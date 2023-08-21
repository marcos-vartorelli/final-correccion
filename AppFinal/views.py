
from django.http import HttpResponse
from django.shortcuts import render 
from AppFinal.models import Sector, Empleado, Cliente, Encargado, Avatar
from AppFinal.forms import SectorForm, EmpleadoForm, ClienteForm, EncargadoForm, User, AvatarFormulario
from AppADM.forms import UserRegisterForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    return render(request,'AppFinal/inicio.html')
@login_required
def sector(request):
    return render(request,'AppFinal/sector.html')
@login_required
def empleado(request):
    return render(request,'AppFinal/empleado.html')
@login_required
def cliente(request):
    return render(request,'AppFinal/cliente.html')
@login_required
def encargado(request):
    return render(request,'AppFinal/encargado.html')

def pagina404(request):
    return render(request,'AppFinal/pagina404.html')


# aca estan los formularios #-----------------------{{{{}}}}}}-------------------------

def sector(request):
    if request.method == 'POST':
        formulario = SectorForm(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            
            sector = Sector(nombre_empleado=informacion['nombre_empleado'],zona_trabajo=informacion['zona_trabajo'])
            sector.save()
            return render(request,'AppFinal/inicio.html')
    else:
        formulario = SectorForm()
           
    return render(request,'AppFinal/sector.html',{'formulario': formulario})

#-----------------------{{{{}}}}}}-------------------------

def empleado(request):
    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            
            empleado = Empleado(nombre_empleado = informacion['nombre_empleado'],apellido_empleado = informacion ['apellido_empleado'], email = informacion ['email'])
            empleado.save()
            return render(request,'AppFinal/inicio.html')
    else:
        formulario = EmpleadoForm()
            
    return render(request,'AppFinal/empleado.html',{'formulario': formulario})

#-----------------------{{{{}}}}}}-------------------------

def cliente(request):
    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            
            cliente = Cliente(nombre_cliente = informacion['nombre_cliente'],
                                apellido_cliente = informacion ['apellido_cliente'],
                                email = informacion ['email'],)
            cliente.save()
            return render(request,'AppFinal/inicio.html')
    else:
        formulario = ClienteForm()
            
    return render(request,'AppFinal/cliente.html',{'formulario': formulario})

#-----------------------{{{{}}}}}}-------------------------

def encargado(request):
    if request.method == 'POST':
        formulario = EncargadoForm(request.POST)
        print(formulario)
        
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            
            encargado = Encargado(nombre_encargado = informacion['nombre_encargado'],
                                apellido_encargado = informacion ['apellido_encargado'],
                                email = informacion ['email'],
                                sector = informacion['sector'],)
            encargado.save()
            return render(request,'AppFinal/inicio.html')
    else:
        formulario = EncargadoForm()
            
    return render(request,'AppFinal/encargado.html',{'formulario': formulario})

#---------estas es la busqueda---------------


def buscarCliente(request):
    return render(request, 'AppFinal/buscarCliente.html')

def buscar(request):
    if request.GET.get('nombre_cliente'): 
        
        #respuesta = f"Estoy buscando el cliente "
       nombre_cliente = request.GET('nombre_cliente')
       clientes = Cliente.objects.filter(nombre_cliente__icontains=nombre_cliente)
       
       return render(request, 'AppFinal/inicio.html',{'nombre_cliente':nombre_cliente})
    else:
        respuesta = "No ingresaste ningun dato"
        
    return render(request, 'AppFinal/inicio.html',{'respuesta':respuesta})



def buscarEmpleado(request):
    return render(request, 'AppFinal/buscarCliente.html')

def buscar(request):
    if request.GET.get('nombre_cliente'): 
        
        #respuesta = f"Estoy buscando el cliente "
       nombre_cliente = request.GET('nombre_cliente')
       clientes = Cliente.objects.filter(nombre_cliente__icontains=nombre_cliente)
       
       return render(request, 'AppFinal/inicio.html',{'nombre_cliente':nombre_cliente})
    else:
        respuesta = "No ingresaste ningun dato"
        
    return render(request, 'AppFinal/inicio.html',{'respuesta':respuesta})


       
  #------ CRUD----------
  
  
       
def verClientes(request):
    cliente = Cliente.objects.all() 
    contexto= {"cliente":cliente} 

    return render(request, "AppFinal/verClientes.html", contexto)


def eliminarCliente(request, nombre_cliente):
 
    cliente = Cliente.objects.get(nombre_cliente = nombre_cliente)
    cliente.delete()
 
    cliente = Cliente.objects.all()  
 
    contexto = {"cliente": cliente}
 
    return render(request, "AppFinal/verClientes.html", contexto)

def editarCliente(request, nombre_cliente):
 
    cliente = Cliente.objects.get(nombre_cliente = nombre_cliente)
    
    if request.method == "POST":
       formulario = ClienteForm(request.POST)
       print(formulario)

       if formulario.is_valid():
           informacion =formulario.cleaned_data
           
           cliente.nombre_cliente = informacion['nombre_cliente']
           cliente.apellido_cliente = informacion['apellido_cliente']
           cliente.email = informacion['email']
           
           cliente.save()
           
           return render(request, 'AppFinal/inicio.html')
            
    else:
        formulario = ClienteForm(initial={'nombre_cliente':cliente.nombre_cliente,
                                          'apellido_cliente':cliente.apellido_cliente, 
                                          'email':cliente.email})        
    return render(request, 'AppFinal/editarCliente.html',{'formulario':formulario, 'nombre_cliente':nombre_cliente})


#-----------------------------

def verEmpleado(request):
    empleado = Empleado.objects.all() 
    contexto= {"empleado":empleado} 

    return render(request, "AppFinal/verEmpleado.html", contexto)

def eliminarEmpleado(request, nombre_empleado):
 
    empleado = Empleado.objects.filter(nombre_empleado = nombre_empleado)
    empleado.delete()
 
    empleado = Empleado.objects.all()  
 
    contexto = {"empleado": empleado}
 
    return render(request, "AppFinal/verEmpleado.html", contexto)

def editarEmpleado(request, nombre_empleado):
 
    empleado = Empleado.objects.get(nombre_empleado = nombre_empleado)
    
    if request.method == "POST":
       formulario = EmpleadoForm(request.POST)
       print(formulario)

       if formulario.is_valid():
           informacion =formulario.cleaned_data
           
           empleado.nombre_empleado = informacion['nombre_empleado']
           empleado.apellido_empleado = informacion['apellido_empleado']
           empleado.email = informacion['email']
           
           empleado.save()
           
           return render(request, 'AppFinal/inicio.html')
            
    else:
        formulario = EmpleadoForm(initial={'nombre_empleado':empleado.nombre_empleado,
                                          'apellido_empleado':empleado.apellido_empleado, 
                                          'email':empleado.email})        
    return render(request, 'AppFinal/editarEmpleado.html',{'formulario':formulario, 'nombre_empleado':nombre_empleado})


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
            avatar.save()

            return render(request, "AppFinal/inicio.html")
    else:
        miFormulario=AvatarFormulario()
        
    return render(request, "AppFinal/agregarAvatar.html", {'miFormulario': miFormulario})

    
  