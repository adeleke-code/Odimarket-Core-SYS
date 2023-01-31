from rest_framework import serializers
from .models import Profile, Post, Catalogue, DirectMessage


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        read_only=True,

    )
    class Meta:
        model = Profile
        fields = [
            'user',
            'name',
            'profile_picture',
            'location',
            'description'
        ]

class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(
        read_only=True,

    )

    class Meta:
        model = Post
        fields = [
            'content',
            'picture',
            'author',
        ]
  

class CatalogueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = [
            'product'
            'picture'
            'description'
        ]


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = [
            'content'
        ]


        

