from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Profile 
import json
from django.http import JsonResponse
from .serializers import ProfileSerializer
# from .serializers import DeviceSerializer

# class DeviceView(APIView):
#     def get(self, request):
#         devices = Device.objects.all()
#         serializer = DeviceSerializer(devices, many=True)
#         return Response({"articles": serializer.data})

#     def post(self, request):
#         device = request.data.get('device')
#         # Create an device from the above data
#         serializer = DeviceSerializer(data=device)
#         if serializer.is_valid(raise_exception=True):
#             device_saved = serializer.save()
#         return Response({"success": "Device '{}' created successfully".format(device_saved.title)})


class SetBytesView(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data[0])

    
    def post(self, request):
        try:
            byte = request.POST.get("byte")
            if len(str(byte)) < 20:
                return JsonResponse("Request data is not correct!", safe=False)
            else:
                p = Profile.objects.get(id=1)
                p.data = byte
                p.save()
                return JsonResponse("Your byte is " + byte, safe=False)
        except ValueError as e:
            return JsonResponse(e.args[0], status.HTTP_404_NOT_FOUND)

    
