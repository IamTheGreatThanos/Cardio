from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'snippets', UserViewSet, basename='userviewset')

urlpatterns = [
    path('login/', Login.as_view()),
    path('create/', Register.as_view()),
    path('get/', UsersGetApi.as_view()),
    path('change/', ChangeUser.as_view()),
    path('delete/<id>', DeleteUser.as_view()),
    path('', include(router.urls)),
]