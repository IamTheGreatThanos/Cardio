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
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


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
                        if h > 16400000:
                            h = 16400000
                        if h < 12400000:
                            h = 12400000
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
            async_to_sync(channel.group_send)(
				group_name,
				{
					'type': 'send_point',
					'content': {
						'pointers': bb,
					}
				}
			)
            if p.data == None:
                p.data = bb[1:]
            elif len(p.data) > 3500:
                p.data = bb[1:]
            else:
                p.data = p.data + bb[1:]
            p.save()
            return JsonResponse({'status': 'ok'})
        except ValueError as e:
            return JsonResponse(e.args[0], status.HTTP_404_NOT_FOUND)


class getData(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id):
        queryset = Profile.objects.values('data').get(device_id = id)
        return Response(queryset)
            
