from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import * 
import json
from django.http import JsonResponse
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework import generics, permissions, status, views
from django.conf import settings


class Login(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        s = LoginSer(data=request.data)
        if s.is_valid():
            username = s.validated_data['username']
            pwd = s.validated_data['pwd']
            user = User.objects.filter(username = username)
            if user.exists():
                user = user[0]
                if not user.check_password(pwd):
                    return Response({'status': 'wrong'})
                t, _ = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        "key": t.key, 
                        "uid": user.id, 
                        "is_staff": user.is_staff,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'location': user.location,
                        'avatar': request.build_absolute_uri(user.avatar.url),
                        'birth_date': user.birth_date
                    }
                )
        else:
            return Response(s.errors)


class Register(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        s = RegSer(data=request.data)
        if s.is_valid():
            u = User.objects.create(
                username = s.validated_data['username'],
                first_name = s.validated_data['first_name'],
                last_name = s.validated_data['last_name'],
                location = s.validated_data['location'],
                avatar = s.validated_data['avatar'],
                birth_date = s.validated_data['birth_date'],
            )
            u.set_password(s.validated_data['pwd'])
            u.save()
            return Response({'status': "ok"})
        else:
            return Response(s.errors)
    