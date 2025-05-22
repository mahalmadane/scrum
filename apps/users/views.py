import logging
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny

from core.utils.logging import handler_creat_view
from .permissions import IsSelf

from apps.users.models import User
from apps.users.serializers import UserSerializer

from .filters import UserFilter
from django_filters.rest_framework import DjangoFilterBackend

logger = logging.getLogger('django')

class UserRegisterCreateView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[AllowAny]
    def create(self, request, *args, **kwargs):
        return handler_creat_view(self, request, *args, **kwargs)
        
   
class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    
    serializer_class=UserSerializer
    permission_classes=[IsSelf]

    

class UserListView(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    # permission_classes=[IsScrumMaster]
    filter_backends=[DjangoFilterBackend]
    filterset_class=UserFilter