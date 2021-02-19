from rest_framework import serializers
from .models import Trainees

class TraineesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainees
        fields = ('id', 'userName', 'workout_type')