from rest_framework import permissions
from django.contrib.auth.backends import BaseBackend
from rest_framework.exceptions import AuthenticationFailed
import requests
import json
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
from django.contrib.auth import get_user_model
User = get_user_model()





class TokenBackend(permissions.BasePermission):

    def has_permission(self, request, view):
        headers = request.headers.get('Authorization')
        if headers is None:
            return None
        try:
            token = headers.split()[1]
            
            url = os.getenv("auth_verify")
            headers = {
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {token}"
                    } 

            response = requests.post(url=url, headers=headers)
            
            if response.status_code == 400:
                raise AuthenticationFailed({"message": "invalid token"})
            else:
                try:

                    auth_data = json.loads(response.text)
                    email = auth_data['data']['email']
                    user = User.objects.get(email=email)

                    request.user = user
                   
                    if user.is_active:
                        return request.user
                    else:
                        False
                except User.DoesNotExist:
                    return False
        except User.DoesNotExist:
            return False
  