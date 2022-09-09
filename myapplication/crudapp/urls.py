from django.urls import path
from . import views

urlpatterns = [
    path('c1/', views.get_homepage),
    path('e1/', views.insert_employee),
    path('d1/', views.delete_employee),
    path('a1/', views.get_AllEmployee),
    path('v1/', views.validation_middleware),
]
