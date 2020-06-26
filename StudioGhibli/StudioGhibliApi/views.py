from rest_framework.response import Response
from StudioGhibliApi.models import Locate, Category
from rest_framework import viewsets
from StudioGhibliApi.serializers import LocateSerializer
import requests


class ListGhibli(viewsets.ViewSet):
    """Основной класс предстваления"""

    type = [  # категории
        'title',
        'director',
        'producer'
    ]

    def get_api(self):
        """Получение информации по api"""
        url = "https://ghibliapi.herokuapp.com/films"
        data = requests.get(url, timeout=1).json()
        return data

    def replacement(self, category):
        """Писк данных в базе и замена"""
        locate = Locate.objects.all()
        api_info = self.get_api()
        for info in locate:
            for cat in category:
                for data in api_info:
                    if info.us_locate.lower() == data[cat].lower():
                        data[cat] = info.ru_locate
        return api_info

    def list(self, request, lang='us'):
        """Предоставление информации"""
        if lang == 'us':
            return Response(self.get_api())
        return Response(self.replacement(self.type))
