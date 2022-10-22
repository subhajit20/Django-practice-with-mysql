from ast import Add
from django.urls import path
from .views import Home,Sending_Mail
urlpatterns = [
    path('r1/',Home ),
    path('r2/',Sending_Mail),
]