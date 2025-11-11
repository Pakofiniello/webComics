from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, Manga

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user','manga_letti','manga_watchlist']


class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['titolo','descrizione','artista','anno','genere','img_url']