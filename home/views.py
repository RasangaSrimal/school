from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')

def gallery(request):
    return render(request, 'home/gallery.html')

def events(request):
    return render(request, 'home/events.html')

def courses(request):
    return render(request, 'home/courses.html')