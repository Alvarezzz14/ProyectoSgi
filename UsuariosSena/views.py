from django.shortcuts import render, HttpResponseRedirect, redirect
# from .forms import LoginForm
from .forms import UsuariosSenaForm, LoginForm, ElementosForm, PrestamosForm


# Create your views here.

def login_view(request):
    return render(request, 'indexLogin.html')

def baseAdmin_view(request):
    return render(request, 'superAdmin/basesuadmin.html')

def registroUsuario_view(request):
    return render(request, 'superAdmin/registroUsuario.html')

def formPrestamos_view(request):
    return render(request, 'superAdmin/formPrestamos.html')

def formElementos_view(request):
    return render(request, 'superAdmin/formElementos.html')

def consultarUsuario_view(request):
    return render(request, 'superAdmin/consultarUsuario.html')


#prueba de loginnnnnnnnnnn
def login_view(request):
    if request.method == 'POST':
        # Procesa el formulario si se envió
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            # Aquí puedes realizar acciones adicionales, como la autenticación
            # Si el formulario es válido, redirige al usuario a la página de inicio o a donde sea necesario.
            return HttpResponseRedirect('baseAdmin_view')
    else:
        # Renderiza un formulario vacío si no se envió uno
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

#Formulario Crear Usuarios

def crear_usuario(request):
    if request.method == 'POST':
        form = UsuariosSenaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')  # Redireccionar a la lista de usuarios
    else:
        form = UsuariosSenaForm()
    
    return render(request, 'formPruebas/crear_usuario.html', {'form': form})

def crear_elemento(request):
    if request.method == 'POST':
        form = ElementosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_elementos')  # Redireccionar a la lista de elementos
    else:
        form = ElementosForm()
    
    return render(request, 'formPruebas/crear_elemento.html', {'form': form})


def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_elementos')  # Redireccionar a la lista de elementos
    else:
        form = PrestamosForm()
    
    return render(request, 'formPruebas/crear_prestamo.html', {'form': form})