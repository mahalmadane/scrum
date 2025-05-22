from django.urls import path, include
from .views import SprintViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'sprints', SprintViewSet, basename='sprint')


urlpatterns = [
    path('', include(router.urls))
]
