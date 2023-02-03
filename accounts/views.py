from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .serializers import UserRegistrationSerializer, LoginSerializer
import requests
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
import json
from django.contrib.auth import authenticate
User = get_user_model()


class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        data['response'] = 'successfully registered a new user.'
        data['email'] = account.email
        data['first_name'] = account.first_name

        return Response(data)




class UserLoginView(APIView):
    def post(self, request):
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(request, email = serializer.validated_data['email'], password = serializer.validated_data['password'])
            print(user)
            if user:
                if not user.is_admin:

                    try:
                        url1 = os.getenv("auth_signin")
                        data = {
                            "user": serializer.validated_data['email'],
                            "password": serializer.validated_data['password'],
                            "product_code": "ODI-MKT"
                        }

                        response = requests.post(url=url1, data=data)
                        status = response.status_code
                        if status == 200:
                            return Response(response, 200)
                        else:
                            return Response({"message": data}, 400)
                    except Exception as e:
                        raise e   
                else:
                    data = {
                        'message'  : "failed",
                        'errors': 'This account is not a user account'
                        }
                    return Response(data, 400)
            else:
                data = {
                    'message'  : "failed",
                    'errors': 'Please provide a valid email and password'
                    }
                return Response(data, 400)

