from django.urls import path, include
from .views import UserRegisterView, UserLoginView










urlpatterns = [
    path('register', UserRegisterView.as_view()),
    path('user', UserLoginView.as_view()),

]