from .models import Anime, Animes
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class AnimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animes
        fields = ['id', 'name', 'genres', 'num_of_eps', 'img']


class AnimeSerializer(serializers.ModelSerializer):
    # anime = AnimesSerializer()
    name = serializers.CharField(source='anime.name')
    genres = serializers.CharField(source='anime.genres')
    num_of_eps = serializers.CharField(source='anime.num_of_eps')
    img = serializers.CharField(source='anime.img')
    owner = serializers.CharField(source='owner.username')
    class Meta:
        model = Anime
        fields = ['id', 'name', 'genres', 'num_of_eps', 'img', 'rating', 'favorite', 'comment', 'current_episode', 'owner', 'status']


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']


class AnimeListSetializer(serializers.ModelSerializer):
    class Meta(object):
        model = Animes
        fields = ['id', 'name', 'genres', 'num_of_eps', 'img']


class PublicListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    id = serializers.IntegerField(source='user.id')
    class Meta:
        model = PublicAnimelist
        fields = ['user', 'id']
