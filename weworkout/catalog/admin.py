from django.contrib import admin

# Register your models here.

from catalog.models import Userprofile, Workout, Exercise

admin.site.register(Userprofile)
admin.site.register(Workout)
admin.site.register(Exercise)