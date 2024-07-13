from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, UserSerializer
from .models import CustomUser
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter


class RegistrationAPIView(APIView):

    def get_queryset(self):
        return CustomUser.objects.none()  # Возвращает пустой QuerySet

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Юзер создан", "user": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['email', 'first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']
    pagination_class = CustomPagination


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
