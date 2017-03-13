import hashlib
import os
import time

import multiuploader.default_settings as DEFAULTS
from django.conf import settings
from django.db import models
from django.utils.text import get_valid_filename
from django.utils.translation import ugettext_lazy as _


def _upload_to(instance, filename):
    upload_path = getattr(settings, 'MULTIUPLOADER_FILES_FOLDER', DEFAULTS.MULTIUPLOADER_FILES_FOLDER)

    if upload_path[-1] != '/':
        upload_path += '/'

    filename = get_valid_filename(os.path.basename(filename))
    filename, ext = os.path.splitext(filename)
    md5hash = hashlib.md5()
    md5hash.update(str(time.time()).encode("utf8"))
    fullname = os.path.join(upload_path, "%s.%s%s" % (filename, md5hash.hexdigest(), ext))

    return fullname


class BaseAttachment(models.Model):
    filename = models.CharField(max_length=255, blank=False, null=False)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % self.filename


class MultiuploaderFile(BaseAttachment):

    file = models.FileField(upload_to=_upload_to, max_length=255)

    def save(self, *args, **kwargs):
        self.filename = os.path.basename(self.file.path)
        return super(MultiuploaderFile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('multiuploader file')
        verbose_name_plural = _('multiuploader files')
