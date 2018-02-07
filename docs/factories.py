from django.contrib.auth import get_user_model
import factory

from . import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = 'regular user'
    email = 'john@doe.com'


class DocumentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Document

    owner = factory.SubFactory(UserFactory)
    title = factory.Sequence(lambda n: "Document_%d" % n)
    content = factory.Sequence(lambda n: "Contentzz_%d" % n)
    can_access = 'ALL'
