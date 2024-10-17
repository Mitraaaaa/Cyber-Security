from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=64, blank=True)
    n_value = models.IntegerField(default=5)
