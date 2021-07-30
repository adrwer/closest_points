from rest_framework import serializers
from .models import Points


class PointsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = [
            "input",
            "output"
        ]
        extra_kwargs = {

        }