# from django.shortcuts import render
from rest_framework import viewsets  # , generics, permissions, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import BlocklogsSerializer
from .models import Backlogs
# from apps.projects.models import Project
# from apps.projects.serializers import ProjectSerializer
from core.permissions import IsProductOwnerOrReadOnly

# Create your views here.


class BlocklogsViewSet(viewsets.ModelViewSet):
    queryset = Backlogs.objects.all()
    serializer_class = BlocklogsSerializer
    permission_classes = [IsProductOwnerOrReadOnly]
