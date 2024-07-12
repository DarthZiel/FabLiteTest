from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, UserSerializer
from .models import CustomUser
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet


class RegistrationAPIView(APIView):

    def get_queryset(self):
        return CustomUser.objects.none()  # Возвращает пустой QuerySet

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Юзер создан", "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

