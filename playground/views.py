#this module is responsible for requests or this is also called a request handler 

#this processes html files
from django.shortcuts import render 
#this processes api requests
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name' : 'Jonah'})