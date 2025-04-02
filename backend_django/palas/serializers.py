from rest_framework import serializers
from .models import Pala

class PalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pala
        fields = '__all__'
