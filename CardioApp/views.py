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
            a = byte[2:len(byte)-1]
            l = len(a)
            s = 0
            bb = []
            a = a.replace('\t','')
            a = a.split('\\x')[1:]
            for i in range(0, len(a)-3, 3):
                b = ''
                b += a[i][:2] + a[i+1][:2] + a[i+2][:2]
                h = int(b, 16)
                bb.append(h)
            # for i in range(12,l+12,12):
            #     t = a[s:i].split("\\x") 
            #     st = ""
                
            #     # st = st.join(t[:2])
            #     st += t[0][:1] + t[1][:2] + t[2][:2] 
            #     h = int(st, 16)
            #     bb.append(h)
            #     s=i
            p.data = bb
            p.save()
            return JsonResponse({'status': 'ok'})
        except ValueError as e:
            return JsonResponse(e.args[0], status.HTTP_404_NOT_FOUND)




    
