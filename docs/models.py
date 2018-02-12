import shortuuid
from django.conf import settings
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

def get_sentinel_user():
    """Return a generic user to assign deleted user accounts' docs to"""
    return User.objects.get_or_create(username='deleted')[0]

class Document(IndexedTimeStampedModel):
    """Represents the Document model."""
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET(get_sentinel_user))
    can_access = models.CharField(
        max_length=20, blank=False, choices=DOC_ACCESS_CHOICES, default=ALL)
    slug = models.SlugField(max_length=255, blank=False, default=shortuuid.uuid)

    def __str__(self):
        """Return a human readable representation of the Document instance."""
        return "{}".format(self.title)
