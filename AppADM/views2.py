from django.shortcuts import render
from AppFinal.forms import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserEditForm, User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


#from AppADM.models import User

# Create your views here.


     
    #-----------------------------
    
def login_request(request):

    if request.method == 'POST':
        form= AuthenticationForm(request, data = request.POST)

        if form.is_valid():  

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppFinal/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppFinal/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppFinal/inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppADM/login.html", {"form": form})


#---------------------------------------------

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppFinal/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppADM/registro.html" ,  {"form":form})
  
  #---------------------------------------------
  
  
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppFinal/inicio.html")

    else:

        formulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppADM/editarPerfil.html", {" formulario": formulario, "usuario": usuario})

  
  