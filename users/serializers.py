from rest_framework import serializers

class LoginSer(serializers.Serializer):
    username = serializers.CharField()
    pwd = serializers.CharField()


class RegSer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    pwd = serializers.CharField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    location = serializers.CharField()
    avatar = serializers.FileField(required=False)
    birth_date = serializers.DateField()
    device_id = serializers.CharField()