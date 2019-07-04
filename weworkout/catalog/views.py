from django.shortcuts import render
from catalog.models import Userprofile, Workout, Exercise
# Create your views here.

def index(request):
    num_wo = Workout.objects.all().count()
    num_ex = Exercise.objects.all().count()
    num_user = Userprofile.objects.all().count()

    context = {
        'nu_wo': num_wo,
        'nu_ex' : num_ex,
        'nu_user' : num_user,
    }
    
    return render(request, 'index.html', context=context)

from django.views import generic

class WorkoutListView(generic.ListView):
    model = Workout

class WorkoutDetailView(generic.DetailView):
    model = Workout