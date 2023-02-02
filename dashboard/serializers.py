from rest_framework import serializers
from .models import Profile, Post, Catalogue, DirectMessage


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField(
        read_only=True,

    )
    class Meta:
        model = Profile
        fields = [
            'id',
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
            'id',
            'content',
            'picture',
            'author',
        ]
  

class CatalogueSerializer(serializers.ModelSerializer):

    owner = serializers.CharField(
        read_only=True,

    )
    class Meta:
        model = Catalogue
        fields = [
            'id',
            'product',
            'picture',
            'description',
            'owner',
            'created_at'
        ]


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = [
            'content'
        ]


        

