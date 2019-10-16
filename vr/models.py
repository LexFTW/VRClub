from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    id_room = models.AutoField(primary_key=True)
    capacity = models.IntegerField()
    location = models.CharField(max_length=200)
    glasses_availables = models.IntegerField();

class Glasses(models.Model):
    id_glasses = models.AutoField(primary_key=True)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    glasses_model = models.CharField(max_length=200)

class Reservation(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    id_person = models.ForeignKey(User, on_delete=models.CASCADE)
    id_room = models.ForeignKey(Room, on_delete=models.CASCADE)
    day = models.DateField()
    init_hour = models.DateTimeField()
    final_hour = models.DateTimeField()
    num_persons = models.IntegerField()

class ReservationGlass(models.Model):
    id_reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    id_glasses = models.ForeignKey(Glasses, on_delete=models.CASCADE)
    stock = models.IntegerField()
