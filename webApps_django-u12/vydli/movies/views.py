from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request=request,template_name='movies/index.html',context={'movies':movies})

def detail(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    return render(request=request,template_name='movies/detail.html',context={'movie':movie})