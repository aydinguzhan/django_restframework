from rest_framework import serializers
from restapi.models import Data


class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    mac = serializers.CharField()
    card = serializers.CharField()
    name = serializers.CharField()
    department = serializers.CharField()
    status = serializers.BooleanField()
    created_info = serializers.DateField()
    updated_info = serializers.DateField(read_only=True)
    last_info = serializers.DateField(read_only=True)


    def create(self, validated_data):
        print(validated_data)
        return Data.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.mac = validated_data.get('mac', instance.mac)
        instance.card = validated_data.get('card', instance.card)
        instance.name = validated_data.get('name', instance.name)
        instance.department = validated_data.get('department', instance.department)
        instance.status = validated_data.get('status', instance.status)
        instance.created_info = validated_data.get('created_info', instance.created_info)

        instance.save()
        return instance
