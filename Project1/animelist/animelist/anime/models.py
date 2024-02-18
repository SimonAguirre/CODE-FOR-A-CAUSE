from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


STATUS_CHOICES = [
    ('Watching', 'Watching'),
    ('Finished', 'Finished'),
    ('Plan to Watch', 'Plan to Watch'),
]

# Create your models here.
class Animes(models.Model):
    name = models.CharField(max_length=200)
    genres = models.CharField(max_length=200)
    num_of_eps = models.IntegerField()
    img = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Anime(models.Model):
    anime = models.ForeignKey(Animes, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=0)
    favorite = models.BooleanField(default=False)
    comment = models.CharField(max_length=1000, default='')
    current_episode = models.IntegerField(default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Watching')

    def __str__(self) -> str:
        return self.anime.name
    

class PublicAnimelist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


admin.site.register(Anime)
admin.site.register(Animes)
admin.site.register(PublicAnimelist)