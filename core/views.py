from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def portafolio(request):
    return render(request, 'core/portafolio.html')

def contact(request):
    return render(request, 'core/contact.html')