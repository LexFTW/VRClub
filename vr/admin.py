from django.contrib import admin

# Register your models here.
from .models import Room, Glasses, Reservation

admin.site.register(Room)
admin.site.register(Glasses)
admin.site.register(Reservation)
