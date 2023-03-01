from rest_framework import serializers
from .models import *


class HomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Home
        fields="__all__"