from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for Tag objects"""

    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_fields_only = ['id', ]