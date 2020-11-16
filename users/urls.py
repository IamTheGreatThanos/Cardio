from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view()),
    path('create/', Register.as_view())
]