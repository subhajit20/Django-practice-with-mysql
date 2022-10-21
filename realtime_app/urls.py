from ast import Add
from django.urls import path
from .views import Home
urlpatterns = [
    path('r1/',Home ),
]