from django.db import models

# Create your models here.
class contact(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()


class Drone(models.Model):
    drone_id = models.IntegerField(primary_key=True)
    drone_slot_id = models.IntegerField()
    location_id = models.IntegerField()

    