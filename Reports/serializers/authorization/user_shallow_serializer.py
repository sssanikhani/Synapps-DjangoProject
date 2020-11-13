from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserShallowSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
        )