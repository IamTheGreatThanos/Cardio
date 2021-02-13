from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view()),
    path('create/', Register.as_view()),
    path('get/', UsersGetApi.as_view()),
    path('change/', ChangeUser.as_view()),
    path('delete/<id>', DeleteUser.as_view())
]