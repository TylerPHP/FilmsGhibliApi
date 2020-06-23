from rest_framework.views import APIView
from rest_framework.response import Response
from StudioGhibliApi.models import Locate
from StudioGhibliApi.serializers import LocateSerializer
import requests


class ListGhibli(APIView):
    """Основной класс предстваления"""
    def get_info(self):

        pass

    def get(self, request):
        """Предоставление информации"""
        locate = Locate.objects.all()
        serializer = LocateSerializer(locate, many=True)
        return Response({"data": serializer.data})
