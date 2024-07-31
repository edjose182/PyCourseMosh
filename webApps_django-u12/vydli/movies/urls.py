from django.urls import path

from . import views #It is better to do it in this way because
                    #someone can use a different path

urlpatterns = [ #This is the URL configuration
    path('', views.index,name='movies_index'),
    path('<int:movie_id>',views.detail,name='movies_detail')
]