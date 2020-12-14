from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Profile 
import json
from django.http import JsonResponse
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework import generics, permissions, status, views



class SetBytesView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data[0])

    
    def post(self, request):
        try:
            byte = request.POST.get("byte")
            print(byte)
            p = Profile.objects.get(id=1)
            a = byte.encode()
            l = len(a)
            s = 0
            bb = []
            for i in range(3,l+3,3):
                h = a[s:i].hex()
                h = int(h, 16)
                bb.append(h)
                s=i
            p.data = bb
            p.save()
            return JsonResponse({'status': 'ok'}, safe=False)
        except ValueError as e:
            return JsonResponse(e.args[0], status.HTTP_404_NOT_FOUND)




    
