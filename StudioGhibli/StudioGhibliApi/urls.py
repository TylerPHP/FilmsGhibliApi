from django.urls import path
from StudioGhibliApi.views import *


urlpatterns = [
    path('list/<str:lang>/', ListGhibli.as_view({'get': 'list'})),
    # path('list/ru', ListGhibli.as_view({'get': 'list'})),
    # path('list/us', ListGhibli.as_view()),
]
