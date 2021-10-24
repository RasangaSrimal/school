from home.models import Principal, VicePrincipal
from django.shortcuts import render

# Create your views here.
def home(request):
    vice_principals = VicePrincipal.objects.all()
    return render(request, 'home/index.html', {'vice_principals':vice_principals})

def contact(request):
    return render(request, 'home/contact.html')

def gallery(request):
    return render(request, 'home/gallery.html')

def events(request):
    return render(request, 'home/events.html')

def courses(request):
    return render(request, 'home/courses.html')

def identity(request):
    return render(request, 'home/identity.html')

def history(request):
    principals = Principal.objects.all()
    return render(request, 'home/history.html', {'principals':principals})
