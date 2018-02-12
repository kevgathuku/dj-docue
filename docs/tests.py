import pytest
from django.test import TestCase

from .models import Document
from .factories import DocumentFactory


@pytest.mark.django_db
def test_creating_doc_increases_docs_count():
    old_count = Document.objects.count()

    # Create a new doc and save it to the DB
    new_doc = DocumentFactory.create()

    # Validate count is increased by 1
    new_count = Document.objects.count()

    assert old_count + 1 == new_count
