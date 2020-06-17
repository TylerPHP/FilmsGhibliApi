from rest_framework import serializers
from StudioGhibliApi.models import Locate


class LocateSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = Locate
        fields = ("title", "director", "produser")
