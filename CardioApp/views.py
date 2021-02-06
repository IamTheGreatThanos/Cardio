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
            # p = Profile.objects.get(id=1)
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
                        bb.append(h)
                # p.data = bb
                # p.save()
                group_name = int(a[:12], 16)
                bb.insert(0, group_name)
            # print(bb)
            async_to_sync(channel.group_send)(
				group_name,
				{
					'type': 'send_point',
					'content': {
						'pointers': bb,
					}
				}
			)
            return JsonResponse({'status': 'ok'})
        except ValueError as e:
            return JsonResponse(e.args[0], status.HTTP_404_NOT_FOUND)




    
