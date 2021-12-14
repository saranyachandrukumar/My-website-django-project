from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'Home.html')
def index(request):
    return render(request, 'index.html')
def gallery(request):
    return render(request, 'gallery.html')
def products(request):
    return render(request, 'products.html')
def Contact(request):
    return render(request, 'Contact.html')
def aboutus(request):
    return render(request, 'aboutus.html')



