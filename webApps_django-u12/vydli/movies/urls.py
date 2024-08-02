from django.urls import path

from . import views #It is better to do it in this way because
                    #someone can use a different path

app_name = 'movies'

urlpatterns = [ #This is the URL configuration
    path('', views.index,name='index'),
    path('<int:movie_id>',views.detail,name='detail')
]