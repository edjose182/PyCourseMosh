from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def index(request):
    output = Movie.objects.all()
    #output = [m.title for m in movies] This is not working
    return HttpResponse(output)