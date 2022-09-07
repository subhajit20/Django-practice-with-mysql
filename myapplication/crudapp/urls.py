from django.urls import path
from . import views

urlpatterns = [
    path('c1/', views.get_homepage),
    path('e1/', views.insert_employee),
]
