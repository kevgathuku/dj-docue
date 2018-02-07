from django.test import TestCase

from .models import Document
from .factories import DocumentFactory


class ModelTestCase(TestCase):
    """This class defines the test suite for the Document model."""

    # def setUp(self):
        # self.document = DocumentFactory.build()

    def test_model_can_create_a_bucketlist(self):
        old_count = Document.objects.count()
        # Create a doc now
        new_doc = DocumentFactory.create()

        # Validate count is increased by 1
        new_count = Document.objects.count()
        self.assertEqual(old_count + 1, new_count)
