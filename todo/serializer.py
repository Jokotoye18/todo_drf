from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.added_by')
    class Meta:
        model = Todo
        fields = ['id', 'title', 'completed', 'owner','timestamp', 'added_by']
        read_only_fields  = ['timestamp', 'added_by', 'completed']