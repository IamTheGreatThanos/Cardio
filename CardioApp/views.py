from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import * 
import json
from django.http import JsonResponse
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework import generics, permissions, status, views
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from datetime import datetime


class SetBytesView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data[0])

    
    def post(self, request):
        group_name = "user"
        channel = get_channel_layer()
        
        try:
            byte = request.POST.get("byte")
            print(byte)
            p = None
            # a = byte[2:len(byte)-1]
            a = byte
            l = len(a)
            bb = []
            if l > 18:
                s = 0
                for i in range(12, len(a), 6):
                    b = ''               
                    b += a[i:i+6]
                    if len(b) == 6:
                        h = int(b, 16)
                        # if h < 10:
                        #     continue
                        # if h>10 and h < 12400000:
                        #     h = 12400000
                        bb.append(h)
                wid = int(a[:12], 16)
                p = Profile.objects.filter(device_id=wid)
                if p.exists():
                    p = p[0]
                else:
                    p = Profile.objects.create(device_id=wid)
                bb.insert(0, wid)
            # print(bb)
            group_name = "room_"+str(wid)
            async_to_sync(channel.group_send) (
				group_name,
				{
					'type': 'send_point',
					'content': {
						'pointers': bb,
					}
				}
			)
            today_d = datetime.now()
            today = f'{today_d.year}-{today_d.month}-{today_d.day}'
            pd = ProfileData.objects.filter(profile = p, date=today)
            if pd.exists():
                pd = pd[0]
                pd.data = pd.data + bb[1:]
                if len(pd.data) > 50000:
                    pd.data = bb[1:]
                pd.save()
            else:
                ProfileData.objects.create(date=today, data = bb[1:], profile=p)
            return JsonResponse({'status': 'ok'})
        except ValueError as e:
            return JsonResponse(e.args[0], status.HTTP_404_NOT_FOUND)


class getData(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id):
        # queryset = ProfileData.objects.values('date', 'data').filter(profile__device_id = id)
        queryset = ProfileData.objects.values('date', "id").filter(profile__device_id = id).order_by('-date')
        return Response(queryset)


class getDataDate(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id):
        # queryset = ProfileData.objects.values('date', 'data').filter(profile__device_id = id)
        queryset = ProfileData.objects.values('data').filter(id = id)
        return Response(queryset)
            
