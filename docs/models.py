import re
import uuid
import base64
from django.db import models  # noqa

from common.models import IndexedTimeStampedModel
from users.models import User

ALL = 'ALL'
ONLY_ME = 'ONLY ME'
STAFF = 'STAFF'
ADMIN = 'ADMIN'

DOC_ACCESS_CHOICES = (
    (ALL, 'All'),
    (ONLY_ME, 'Only Me'),
    (STAFF, 'Staff'),
    (ADMIN, 'Admin'),
    )


def uuid_url64():
    """Returns a unique, 16 byte, URL safe ID by combining UUID and Base64
    """
    rv = base64.b64encode(uuid.uuid4().bytes).decode('utf-8')
    return re.sub(r'[\=\+\/]', lambda m: {'+': '-', '/': '_', '=': ''}[m.group(0)], rv)

def get_sentinel_user():
    """Return a generic user to assign deleted user accounts' docs to"""
    return User.objects.get_or_create(username='deleted')[0]

class Document(IndexedTimeStampedModel):
    """Represents the Document model."""
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    can_access = models.CharField(
        max_length=20, blank=False, choices=DOC_ACCESS_CHOICES, default=ALL)
    slug = models.SlugField(max_length=255, blank=False, default=uuid_url64)

    def __str__(self):
        """Return a human readable representation of the Document instance."""
        return "{}".format(self.title)
