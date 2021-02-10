from django.urls import path
from .views import *

app_name = "Cardio"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('setByte/', SetBytesView.as_view()),
    path('get/<id>', getData.as_view())
]