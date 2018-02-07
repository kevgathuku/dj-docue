from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    owner = serializers.ReadOnlyField(source='owner.email')
    url = serializers.HyperlinkedIdentityField(
        view_name='document-detail',
        lookup_field='slug'
    )

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Document
        fields = (
            'title',
            'content',
            'can_access',
            'owner',
            'created',
            'modified',
            'url'
        )
        read_only_fields = ('slug', 'created', 'modified')
