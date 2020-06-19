from django.urls import path
from .views import DeviceView, SetBytesView

app_name = "Cardio"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('devices/', DeviceView.as_view()),
    path('setByte/', SetBytesView.as_view()),
]