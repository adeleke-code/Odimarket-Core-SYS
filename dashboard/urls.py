from django.urls import path, include
from rest_framework import routers
from .views import ProfileView, PostCreateView, CatalogueView, UserPostList, ProfileUpdateView



router = routers.DefaultRouter()

# router.register(r'post', PostCreateView)



urlpatterns = [
    path('', include(router.urls)),
    path('profile', ProfileView.as_view()),
    path('cata', CatalogueView.as_view()),
    path('post', PostCreateView.as_view()),
    path('posts', UserPostList.as_view()),
    path('profile/update', ProfileUpdateView.as_view())


]
