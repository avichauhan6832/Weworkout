from django.shortcuts import render
from catalog.models import Userprofile, Workout, Exercise
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    num_wo = Workout.objects.all().count()
    num_ex = Exercise.objects.all().count()
    num_user = Userprofile.objects.all().count()
    print(request.user)
    curr_user = User.objects.get(username=request.user)
    user_workout = Workout.objects.filter(user = curr_user)
    # for w in user_workout.all():
    #     print(w.title)

    context = {
        'nu_wo': num_wo,
        'nu_ex' : num_ex,
        'nu_user' : num_user,
        'workout_list' : user_workout,
    }
    
    return render(request, 'index.html', context=context)

from django.views import generic

class WorkoutListView(generic.ListView):
    model = Workout
    paginate_by = 10

class WorkoutDetailView(generic.DetailView):
    model = Workout

class ExerciseListView(generic.ListView):
    model = Exercise
    paginate_by = 10

class ExerciseDetailView(generic.DetailView):
    model = Exercise
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Workout
from django.contrib.auth.mixins import PermissionRequiredMixin

class WorkoutCreate(PermissionRequiredMixin, CreateView):
    model = Workout
    fields = '__all__'
    initial = {'sets': 0}
    permission_required = 'catalog.can_mark_returned'

class WorkoutUpdate(PermissionRequiredMixin, UpdateView):
    model = Workout
    fields = ['title', 'sets', 'notes', 'exercise', 'upvotes']
    permission_required = 'catalog.can_mark_returned'

class WorkoutDelete(PermissionRequiredMixin, DeleteView):
    model = Workout
    success_url = reverse_lazy('workouts')
    permission_required = 'catalog.can_mark_returned'
