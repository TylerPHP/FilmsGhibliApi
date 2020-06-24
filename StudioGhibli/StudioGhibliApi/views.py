from rest_framework.views import APIView
from rest_framework.response import Response
from StudioGhibliApi.models import Locate
from rest_framework import viewsets
from StudioGhibliApi.serializers import LocateSerializer
import requests


class ListGhibli(viewsets.ViewSet):
    """Основной класс предстваления"""
    def get_api(self):
        """Получение информации по api"""
        url = "https://ghibliapi.herokuapp.com/films"
        data = requests.get(url, timeout=1).json()
        return data

    def replacement(self):
        """Писк данных в базе и замена"""
        locate = Locate.objects.all()
        api_info = self.get_api()[0]
        for info in locate:
            print(api_info['title'])
            if info.us_locate == api_info['title']:
                pass
        return api_info

    def list(self, request):
        """Предоставление информации"""
        self.replacement()
        return Response(self.replacement())
