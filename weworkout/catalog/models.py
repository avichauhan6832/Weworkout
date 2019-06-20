from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Userprofile(models.Model):
    """Model representing a User profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=500, blank=True)
    followers = models.ManyToManyField(User, related_name='followers')
    following = models.ManyToManyField(User, related_name='following')
    workout = models.ManyToManyField('Workout', related_name='user_workout', blank=True)

    def __str__(self):
        return self.user.username

class Workout(models.Model):
    title = models.TextField(max_length=100)
    sets = models.IntegerField(default=0)
    notes = models.TextField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ManyToManyField('Exercise', related_name='wrokout_exercise')
    upvotes = models.ManyToManyField(Userprofile,related_name='upvotes')

    def __str__(self):
        return self.title

class Exercise(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.name


