from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class HH(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    owners = models.ManyToManyField(Owner, related_name='hh_owned')

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=100)
    hh = models.ForeignKey(HH,on_delete=models.CASCADE)
    price_per_night = models.FloatField()
    availability = models.BooleanField(default=True)
    checkin_time = models.TimeField()
    checkout_time = models.TimeField()
    rules = models.TextField()
    

