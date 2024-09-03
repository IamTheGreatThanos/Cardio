from rest_framework import serializers
from .models import User
class LoginSer(serializers.Serializer):
    username = serializers.CharField()
    pwd = serializers.CharField()
    status = serializers.CharField()


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

class RegSe2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        ava = validated_data.get('avatar', None)
        user = super(RegSe2, self).create(validated_data)
        if ava:
            user.avatar = ava
        user.set_password(validated_data['password'])
        user.save()
        return user