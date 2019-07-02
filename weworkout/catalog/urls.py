from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.allworkouts, name='allworkouts'),
    path('', views.allexercises, name='allexercises'),
]
