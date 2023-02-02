from django.urls import path, include
from rest_framework import routers
from .views import ProfileView, PostCreateView, CatalogueView, Update, CatalogueUpdate



router = routers.DefaultRouter()

# router.register(r'post', PostCreateView)



urlpatterns = [
    path('', include(router.urls)),
    path('profile', ProfileView.as_view()),
    path('catalogue', CatalogueView.as_view()),
    path('post', PostCreateView.as_view()),
    path('post/<int:pk>', Update.as_view()),
     path('catalogue/<int:pk>', CatalogueUpdate.as_view())


]
