from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('workouts/', views.WorkoutListView.as_view(), name='workouts'),
    path('workout/<int:pk>', views.WorkoutDetailView.as_view(), name='workout-detail'),
    path('exercises/', views.ExerciseListView.as_view(), name='exercises'),
    path('exercise/<int:pk>', views.ExerciseDetailView.as_view(), name='exercise-detail'),
]
