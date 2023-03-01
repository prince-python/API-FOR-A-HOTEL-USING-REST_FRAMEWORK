from django.shortcuts import render
from . serializers import HomeSerializer
from rest_framework import viewsets
from .models import *


class HomeViewset(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer