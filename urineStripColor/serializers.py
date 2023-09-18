from rest_framework import serializers
from .models import StripImage


class StripImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StripImage
        fields = "__all__"
