from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allworkouts', views.allworkouts, name='allworkouts'),
    path('allexercises', views.allexercises, name='allexercises'),
]
