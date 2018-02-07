from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Document
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')
