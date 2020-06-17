from django.urls import path
from StudioGhibliApi.views import *


urlpatterns = [
    path('list/', ListGhibli.as_view()),
]
