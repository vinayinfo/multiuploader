from django.conf.urls import url
from multiuploader.views import MultiuploaderView

urlpatterns = [
    url(r'^multiuploader_file/(?P<pk>[0-9]+)/$', MultiuploaderView.as_view(), name='multiuploader_file_link'),
    url(r'^multiuploader/$', MultiuploaderView.as_view(), name='multiuploader'),
]
