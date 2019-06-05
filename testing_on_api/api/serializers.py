from rest_framework import serializers
from .models import API

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = API
        fields = ('name', 'age', 'position', 'company', 'created', 'updated')
