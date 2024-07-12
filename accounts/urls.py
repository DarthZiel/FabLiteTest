from django.urls import path, include
from .views import RegistrationAPIView, UserListAPIView
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

urlpatterns = [
    path('api/v1/user/<int:pk>/',
         UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
    path("api/v1/registration/", RegistrationAPIView.as_view()),
    path("api/v1/users/", UserListAPIView.as_view()),
]
