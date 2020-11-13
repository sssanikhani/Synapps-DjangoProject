from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from Reports.serializers.base_serializer import BaseSerializer

class UserShallowSerializer(ModelSerializer, BaseSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
        )