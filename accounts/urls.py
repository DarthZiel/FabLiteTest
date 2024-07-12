from django.contrib import admin
from django.urls import path
from .views import RegistrationAPIView

urlpatterns = [
    path("api/v1/registration/", RegistrationAPIView.as_view()),
]
