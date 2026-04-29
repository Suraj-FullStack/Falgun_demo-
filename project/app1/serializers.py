from rest_framework import serializers
from .models import category, Table

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id', 'name', 'description']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'seats', 'is_available']