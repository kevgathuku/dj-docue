from django.shortcuts import render
from rest_framework import generics, permissions

from .serializers import DocumentSerializer
from .models import Document


class DocumentList(generics.ListCreateAPIView):
    """Manages creating and listing Documents from our REST API."""
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """Save the post data when creating a new Document."""
        serializer.save(owner=self.request.user)


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    lookup_field = 'slug'
