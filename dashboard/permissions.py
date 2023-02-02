from rest_framework import permissions
from django.contrib.auth.backends import BaseBackend
from rest_framework.exceptions import AuthenticationFailed
import requests
import json
from django.contrib.auth import get_user_model
User = get_user_model()





class TokenBackend(permissions.BasePermission):

    def has_permission(self, request, view):
        headers = request.headers.get('Authorization')
        if headers is None:
            return None
        try:
            token = headers.split()[1]
            
            url = 'http://18.207.205.10/auth/auth/verify'
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
                    # print(user)
                    # print(user.__dir__())
                    if user.is_active:
                        return request.user
                    else:
                        False
                except User.DoesNotExist:
                    return False
        except User.DoesNotExist:
            return False
    # def authenticate(self, request, token=None):
    #     headers = request.headers.get('Authorization')
    #     if headers is None:
    #         return None
    #     try:
    #         token = headers.split()[1]
            
    #         url = 'http://18.207.205.10/auth/auth/verify'
    #         headers = {
    #                     "Content-Type": "application/json",
    #                     "Authorization": f"Bearer {token}"
    #                 } 

    #         response = requests.post(url=url, headers=headers)

    #         auth_data = json.loads(response.text)
    #         print(auth_data)
            
    #         email = auth_data['data']['email']
            
    #         user = User.objects.get(email=email)
    #         if user.is_active:
    #             return user
    #     except User.DoesNotExist:
    #         print("IM HERE")
    #         return None

    # def get_user(self, user_id):
    #     try:
    #         return User.objects.get(pk=user_id)
    #     except User.DoesNotExist:
    #         return None




# class IsUser(permissions.BasePermission):
#     print("Hey I'm here")
#     """
#     Allows access only to delivery admin users.
#     """

#     def has_permission(self, request, view):
#         print("MONI")
#         if request.user.is_authenticated:
#             return bool(request.user) 
#         else:
#             raise AuthenticationFailed(detail="Authentication credentials were not provided oh ")