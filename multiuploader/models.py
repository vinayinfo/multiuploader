from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class MultiuploaderFile(models.Model):
    file = models.FileField(upload_to=settings.MULTIUPLOADER_FILES_FOLDER, max_length=255)
    filename = models.CharField(max_length=255, blank=False, null=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('multiuploader file')
        verbose_name_plural = _('multiuploader files')
