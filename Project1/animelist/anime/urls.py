from django.urls import path 
from django.http import HttpResponse
from .views import AnimeView, SignupView, LoginView, AnimeListView, SetListPublicView
from .views import *
urlpatterns = [
    path('mylist', AnimeView.as_view()),
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogOutView.as_view()),
    path('username', UsernameView.as_view()),
    path('set-public-status', SetListPublicView.as_view()),
    path('animelist', AnimeListView.as_view()),
    path('animelist/<int:pk>', AnimelistDetailView.as_view()),
    path('add-anime', AddAnimeView.as_view()),
    path('mylist/<int:pk>/update-anime', UpdateAnimeView.as_view()),
    path('mylist/<int:pk>/delete-anime', DeleteAnimeView.as_view()),
    path('mylist/<int:pk>/', AnimeDetailView.as_view()),
    path('public-list', ListPublicView.as_view()),
    path('public-list/<int:pk>', PublicUserListView.as_view()),
    path('public-list/detail/<int:pk>', PublicUserDetailView.as_view()),
]