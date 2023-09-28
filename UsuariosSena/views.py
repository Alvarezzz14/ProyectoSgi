from django.shortcuts import render

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

