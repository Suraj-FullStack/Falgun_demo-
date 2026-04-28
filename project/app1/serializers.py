from rest_framework import serializers
from .models import category, Menu, Table, Order
    
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = ['id', 'name', 'description']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'seats', 'is_available']    

 