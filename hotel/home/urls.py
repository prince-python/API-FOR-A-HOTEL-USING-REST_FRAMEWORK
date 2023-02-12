from django.urls import path,include
from .views import *
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register(r'Home',HomeViewset)

urlpatterns = [
    path('',include(routers.urls))
]