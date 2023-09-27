from django.shortcuts import render

# Create your views here.

def baseAdmin_view(request):
    return render(request, 'superAdmin/basesuadmin.html')

def login_view(request):
    return render(request, 'indexLogin.html')