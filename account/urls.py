from django.urls import path
from .views import CreateAccount,Login,HomePage,CreateNote,IAM

urlpatterns = [
    path('a1/createaccount',CreateAccount),
    path('a1/getstudent',Login),
    path('a1/home',HomePage),
    path('a1/createblog',CreateNote),
    path('a1/user',IAM)
]