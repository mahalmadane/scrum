# from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SprintSerializer
from .models import Sprint
# from core.permissions import IsScrumMaster
from apps.users.permissions import IsSelf


class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer
    permission_classes = [IsSelf, IsAuthenticated]
