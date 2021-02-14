from rest_framework import serializers
from .models import messgae


class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = messgae
        fields = ['name', 'message', ]
