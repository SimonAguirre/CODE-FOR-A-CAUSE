from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=200)
    rating = models.IntegerField()
    favorite = models.BooleanField()
    comment = models.CharField(max_length=1000)
    current_episode = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Animes(models.Model):
    name = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)
    num_of_eps = models.IntegerField()
    img = models.CharField(max_length=200)

admin.site.register(Anime)
admin.site.register(Animes)