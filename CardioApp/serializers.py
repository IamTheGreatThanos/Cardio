from rest_framework import serializers

# from .models import Device

# class DeviceSerializer(serializers.Serializer):
#     number = serializers.CharField(max_length=120)
#     description = serializers.CharField()
#     owner = serializers.CharField()
#     author_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Device.objects.create(**validated_data)