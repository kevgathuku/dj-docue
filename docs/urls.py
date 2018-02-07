from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DocumentList, DocumentDetail


urlpatterns = [
    url(r'documents/$', DocumentList.as_view(), name="create"),
    url(r'documents/(?P<slug>[-\w]+)/$',
        DocumentDetail.as_view(), name="document-detail"),
]
