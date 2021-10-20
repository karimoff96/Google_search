from django.db import models

# Create your models here.
class Calc(models.Model):
    user_id = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    step = models.IntegerField(default=0)


class Bot_user(models.Model):
    user_id = models.IntegerField(default=0, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50)
    location = models.CharField(max_length=200)


