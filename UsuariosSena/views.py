from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm

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
