from rest_framework import serializers

from .models import User, AdPopup


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name"]


class AdPopupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdPopup
        fields = ["id", "text"]
