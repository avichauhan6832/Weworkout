from django.db import models
from django.urls import reverse

# Create your models here.

from django.contrib.auth.models import User

class Userprofile(models.Model):
    """Model representing a User profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=500, null=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    workout = models.ManyToManyField('Workout', related_name='user_workout', blank=True)

    def __str__(self):
        return self.user.username

class Workout(models.Model):
    title = models.TextField(max_length=100)
    sets = models.IntegerField(default=0)
    notes = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ManyToManyField('Exercise', related_name='wrokout_exercise')
    upvotes = models.ManyToManyField(Userprofile,related_name='upvotes', blank=True)

    def get_absolute_url(self):
        return reverse('workout-detail', args=[str(self.id)])

    def __str__(self):
        return self.title

class Exercise(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=200, blank=True)

    def get_absolute_url(self):
        return reverse('exercise-detail', args=[str(self.id)])

    def __str__(self):
        return self.name



