from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .serializers import UserRegistrationSerializer, LoginSerializer
import requests
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




# class CreateClientView(APIView):
#     def post(self, request):
#         serializer = UserRegistrationSerializer(data=request.data) 
#         if serializer.is_valid(raise_exception=True):

#             try:
#                 url = "http://18.207.205.10/auth/user/create"
#                 data= {
#                 "first_name": serializer.validated_data['first_name'],
#                 "last_name": serializer.validated_data['last_name'],
#                 "email": serializer.validated_data['email'],
#                 "phone": serializer.validated_data['phone'],
#                 "password": serializer.validated_data['password'],
#                 "product_code": serializer.validated_data['product_code'],
#                 "client": serializer.validated_data['client'],
#                 "role": serializer.validated_data['role'],
#                 }

#                 response = requests.post(url=url, data=data)
#                 status = response.status_code
#                 if status == 400:
#                     return Response({'message': 'user already exists'}, status=400)
#                 else:
#                     serializer.create(validate_data=serializer.validated_data)
#                 return Response(response)
#             except requests.exceptions.InvalidSchema:
#                 print("The URL you provided is not a valid URL. Please check the URL and try again.")
#         return ValidationError
                
        
        


class UserLoginView(APIView):
    def post(self, request):
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = authenticate(request, email = serializer.validated_data['email'], password = serializer.validated_data['password'])
            print(user)
            if user:
                if not user.is_admin:

                    try:
                        url1 = "http://18.207.205.10/auth/auth/signin"
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

