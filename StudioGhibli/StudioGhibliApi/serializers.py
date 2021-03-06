from rest_framework import serializers
from StudioGhibliApi.models import Locate


class LocateSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = Locate
        fields = ('ru_locate', 'us_locate', 'category')
