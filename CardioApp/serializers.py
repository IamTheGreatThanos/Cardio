from rest_framework import serializers
from .models import Profile
# from .models import Device

# class DeviceSerializer(serializers.Serializer):
#     number = serializers.CharField(max_length=120)
#     description = serializers.CharField()
#     owner = serializers.CharField()
#     author_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Device.objects.create(**validated_data)

class ProfileSerializer(serializers.Serializer):
    data = serializers.CharField(allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)


class LoginSer(serializers.Serializer):
    username = serializers.CharField()
    pwd = serializers.CharField()


class PDSer(serializers.Serializer):
    date = serializers.CharField()
    data = serializers.CharField()