from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Device
from rest_framework import status

import json
from django.http import JsonResponse
from .serializers import DeviceSerializer

class DeviceView(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        device = request.data.get('device')
        # Create an device from the above data
        serializer = DeviceSerializer(data=device)
        if serializer.is_valid(raise_exception=True):
            device_saved = serializer.save()
        return Response({"success": "Device '{}' created successfully".format(device_saved.title)})


class SetBytesView(APIView):
    def post(self, request):
        devices = Device.objects.all()
        try:
            byte = request.POST.get("byte")
            if len(str(byte)) < 20:
                return JsonResponse("Request data is not correct!", safe=False)
            else:
                return JsonResponse("Your byte is " + byte, safe=False)
        except ValueError as e:
            return JsonResponse(e.args[0], status.HTTP_404_NOT_FOUND)

