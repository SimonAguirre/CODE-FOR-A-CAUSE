from django.urls import path 
from django.http import HttpResponse
from .views import AnimeView, SignupView, LoginView, AnimeListView
from .views import *
urlpatterns = [
    path('', AnimeView.as_view()),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('animelist', AnimeListView.as_view()),
    path('username', UsernameView.as_view()),
]