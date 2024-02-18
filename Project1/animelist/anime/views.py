# from rest_framework
from django.http import JsonResponse, HttpResponse
from .models import Anime, Animes, PublicAnimelist
from .serializers import AnimeSerializer, UserSerializer, AnimeListSetializer
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView


class AnimeListView(APIView):
    def get(self, request):
        animes = Animes.objects.all()[:50]
        serializer = AnimeListSetializer(animes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UsernameView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user = Token.objects.get(key=token).user.username

        return Response(user, status=status.HTTP_200_OK)


class AnimeView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # token = requst.data['token']
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]

        anime = Anime.objects.filter(owner=Token.objects.get(key=token).user)
        serializer = AnimeSerializer(anime, many=True)

        return JsonResponse(serializer.data, safe=False)
    

class AddAnimeView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        body = request.data
        anime = None

        try:
            id = body['id']
            rating = body['rating']
            favorite = body['favorite']
            comment = body['comment']
            owner = request.user
            watch_status = body['status']
            
            
            if not body['id'] == -1:
                try:
                    anime = Animes.objects.get(id=id)
                except:
                    Response(status=status.HTTP_404_NOT_FOUND)
            else:
                name = body['name']
                genres = body['genres']
                num_of_eps = body['num_of_eps']
                img = body['img']
                anime = Animes(name=name, genres=genres, num_of_eps=num_of_eps, img=img)
                anime.save()

            new_entry = Anime(anime=anime, rating=rating, favorite=favorite, comment=comment, owner=owner, status=watch_status)
            new_entry.save()
            return Response(status=status.HTTP_200_OK)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UpdateAnimeView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        anime = None
        try:
            anime = Anime.objects.get(id=pk)
        except Anime.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            if not anime.owner == request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            
            body = request.data
            rating = body['rating']
            favorite = body['favorite']
            comment = body['comment']
            current_episode = body['current_episode']
            watch_status = body['status']

            anime.rating = rating
            anime.favorite = favorite
            anime.comment = comment
            anime.current_episode = current_episode
            anime.status = watch_status

            anime.save()
            return Response(status=status.HTTP_202_ACCEPTED)

        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class DeleteAnimeView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        anime = None
        try:
            anime = Anime.objects.get(id=pk)
        except Anime.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if not anime.owner == request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        anime.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    


class AnimeDetailView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        anime = None
        try:
            anime = Anime.objects.get(id=pk)
        except Anime.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if not anime.owner == request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnimelistDetailView(APIView):
     def get(self, request, pk):
        anime = None
        try:
            anime = Animes.objects.get(id=pk)
        except Anime.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AnimesSerializer(anime)
        return Response(serializer.data, status=status.HTTP_200_OK)

            

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response('Incorrext username or password', status=status.HTTP_200_OK)

        token, c = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({"token": token.key, "user":serializer.data['username']})

class LogOutView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
            token_db = Token.objects.get(key=token)
            token_db.delete()
            return Response(status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            

class SetListPublicView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            is_public = request.data['public']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        user = Token.objects.get(key=token).user
        if is_public:
            user, c = PublicAnimelist.objects.get_or_create(user=user)
            return Response('set to public', status=status.HTTP_200_OK)
        else:
            try:
                user_ro_be_deleted = PublicAnimelist.objects.get(user=user)
                user_ro_be_deleted.delete()
            except PublicAnimelist.DoesNotExist:
                return Response('set to private', status=status.HTTP_200_OK)

            return Response('set to private', status=status.HTTP_200_OK)
    


class ListPublicView(APIView):
    def get(self, request):     
        users = PublicAnimelist.objects.all()
        serializer = PublicListSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PublicUserListView(APIView):
    def get(self, post, pk):
        user = None
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            authorized = PublicAnimelist.objects.get(user=user)
        except PublicAnimelist.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        animes = Anime.objects.filter(owner=user)
        serializer = AnimeSerializer(animes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class PublicUserDetailView(APIView):    
    def get(self, request, pk):
        anime = None
        user = None
       
        try:
            anime = Anime.objects.get(id=pk)
        except Anime.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            authorized = PublicAnimelist.objects.get(user=anime.owner)
        except PublicAnimelist.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        
        serializer = AnimeSerializer(anime)
        return Response(serializer.data, status=status.HTTP_200_OK)

    

    
