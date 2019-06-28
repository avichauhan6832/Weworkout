from django.shortcuts import render
from catalog.models import Userprofile, Workout, Exercise
# Create your views here.

def index(request):
    num_wo = Workout.objects.all().count()
    num_ex = Exercise.objects.all().count()

    context = {
        'number_of_workouts': num_wo,
        'number_of_exercise' : num_ex,
    }
    
    return render(request, 'index.html', context=context)
