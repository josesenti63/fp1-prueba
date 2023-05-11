from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
#Mensaje que devuelve la home:
def home_page_view(request):
    return HttpResponse("Hola Futbol Pepe")
