from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

def index(request):
    movies = Movie.objects.all()
    return render(request=request,template_name='movies/index.html',context={'movies':movies})

def detail(request,movie_id):
    movie = get_object_or_404(Movie,pk=movie_id)
    return render(request=request,template_name='movies/detail.html',context={'movie':movie})