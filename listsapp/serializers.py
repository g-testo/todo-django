from django.db import models
from rest_framework import serializers
from .models import List, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name','due_date','is_complete', 'list_id']

class ListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = ['id','name','items']