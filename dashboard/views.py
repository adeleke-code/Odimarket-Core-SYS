from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth import get_user_model
from accounts.models import User
from rest_framework.response import Response
from .serializers import ProfileSerializer, PostSerializer, CatalogueSerializer, DirectMessageSerializer
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import generics
from .models import Post, Catalogue, Profile
from .permissions import IsUser
from .permissions import TokenBackend
from django.core.exceptions import ValidationError


User = get_user_model()
# Create your views here.

class ProfileView(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (TokenBackend,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        profile = serializer.save(user=request.user)
        data['response'] = 'successfully created a profile.'
        data['name'] = profile.name
        data['location'] = profile.location

        return Response(data)
    def get(self, request):

        user = Profile.objects.all().filter(user=request.user)
        serializer = ProfileSerializer(user, many=True)
        
        return Response(serializer.data)

    # def put(self, request, *args, **kwargs):
    #     profile = Profile.objects.get(user=request.user)
    #     profile_data = JSONParser().parse(request) 
    #     serializer = ProfileSerializer(profile, data=profile_data) 
    #     if serializer.is_valid(): 
    #         serializer.save() 
    #         return Response(serializer.data) 
    #     return Response(serializer.errors, 400)
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class ProfileUpdateView(generics.UpdateAPIView):
    permission_classes = (TokenBackend,)
    def put(self, request):
        try:
            instance = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return JsonResponse({'error': 'profile not found'}, status=404)

        serializer = ProfileSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

        
class PostCreateView(APIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (TokenBackend,)
   
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                serializer.save(author=request.user)
                data = {}
                data['response'] = 'successfully created a post'
                data['data'] = serializer.data
                return Response(data)
                
            except ValidationError:
                return Response({"message": "validation error!!"})
 
class UserPostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (TokenBackend,)
    def get(self, request):

        all_post = Post.objects.all().filter(author=request.user)
        serializer = PostSerializer(all_post, many=True)
        
        return Response(serializer.data)










class CatalogueView(APIView):
    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer
    permission_classes = (TokenBackend,)


    def get(self, request, *args, **kwargs):
        print(request.user)
        users = User.objects.all()
        print(users, "/n")
        return Response({"users": "all users"}, 200)




# from rest_framework.generics import ListAPIView
# from rest_framework.response import Response
# from .models import MyModel
# from .serializers import MyModelSerializer

# class MyListView(ListAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MyModelSerializer

#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)


# @api_view(["GET"])
# @authentication_classes([TokenBackend])
# @permission_classes([IsUser])
# def catalogueview(request):
#     if request.method == "GET":
#         auth_class = TokenBackend.auth(request)
#         user = auth_class.user
#     x = TokenBackend.auth(request)
#     return Response({"message": "working"})





# from rest_framework import permissions
# from .models import Clients
# import requests
# import json
# class IsAuthenticated(APIView):
#     def post(self, request):
#         header = request.headers.get('Authorization')
#         if header is None:
#             return None
#         token = header.split()[1]
#         url = 'http://18.207.205.10/auth/auth/verify'
#         headers = {
#                     "Content-Type": "application/json",
#                     "Authorization": f"Bearer {token}"
#                 } 

#         response = requests.post(url=url, headers=headers)
#         status = response.status_code

#         # return Response(response)

#         if status == 200:
#             return Response(True)

#         else:
#             return Response({'message': 'verification failed'}, 400)



#         # return request.user.is_authenticated and request.user.is_active
