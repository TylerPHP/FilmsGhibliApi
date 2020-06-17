from rest_framework.views import APIView
from rest_framework.response import Response
from StudioGhibliApi.models import Locate
from StudioGhibliApi.serializers import LocateSerializer


class ListGhibli(APIView):
    """Команата чата"""
    def get(self, request):
        roms = Locate.objects.all()
        serializer = LocateSerializer(roms, many=True)
        return Response({"data": serializer.data})
