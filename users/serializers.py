from rest_framework import serializers

class LoginSer(serializers.Serializer):
    username = serializers.CharField()
    pwd = serializers.CharField()


class RegSer(serializers.Serializer):
    username = serializers.CharField()
    pwd = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    location = serializers.CharField()
    avatar = serializers.FileField()
    birth_date = serializers.DateField()