from rest_framework import serializers

from users.models import TGUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TGUser
        fields = ['id', 'role', 'events']
