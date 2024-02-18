from .models import Anime, Animes
from django.contrib.auth.models import User
from rest_framework import serializers

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['name', 'genre', 'rating', 'favorite', 'comment', 'current_episode', 'owner', 'status']


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']


class AnimeListSetializer(serializers.ModelSerializer):
    class Meta(object):
        model = Animes
        fields = ['name', 'genres', 'num_of_eps', 'img']
