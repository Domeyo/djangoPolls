from django.shortcuts import render
from django.http import HttpResponse

def index(request):
     return HttpResponse('Hello, Alfred when are we getting married')

# Create your views here.
