from __future__ import unicode_literals

from django.conf.urls import url
from multiuploader.views import MultiuploaderView

urlpatterns = [
    url(r'^multiuploader/(?P<pk>[0-9]+)/$', MultiuploaderView.as_view(), name='multiuploader'),
    url(r'^multiuploader/$', MultiuploaderView.as_view(), name='multiuploader'),
]
