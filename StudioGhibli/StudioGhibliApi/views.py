from rest_framework.response import Response
from StudioGhibliApi.models import Locate, Category
from rest_framework import viewsets
from StudioGhibliApi.serializers import LocateSerializer
import requests


class ListGhibli(viewsets.ViewSet):
    """Основной класс предстваления"""
    type = ['title', 'director', 'producer']

    def get_api(self):
        """Получение информации по api"""
        url = "https://ghibliapi.herokuapp.com/films"
        data = requests.get(url, timeout=1).json()
        return data

    # def one_category(self, item):
    #     """Замена только одной категории"""
    #     locate = Locate.objects.all()
    #     api_info = self.get_api()
    #     for info in locate:
    #         for data in api_info:
    #             if info.us_locate.lower() == data['title'].lower():
    #                 data['title'] = info.ru_locate
    #     return api_info

    def query_sql(self):
        """запросы к базе"""
        locate = Locate.objects.filter(category_id__category='title')
        print(locate[1].ru_locate)

    def replacement(self, category):
        """Писк данных в базе и замена"""
        self.query_sql()
        locate = Locate.objects.all()
        api_info = self.get_api()
        for info in locate:
            for cat in category:
                for data in api_info:
                    if info.us_locate.lower() == data[cat].lower():
                        data[cat] = info.ru_locate
        return api_info

    def list(self, request):
        """Предоставление информации"""
        return Response(self.replacement(self.type))
