from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')
    class Meta:
        model = Todo
        fields = ['id',  'title', 'completed','timestamp', 'added_by']
        read_only_fields  = ['timestamp', 'added_by', 'completed']