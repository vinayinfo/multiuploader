import os
import time
from hashlib import sha1

import multiuploader.default_settings as DEFAULTS
from django.conf import settings
from django.db import models
from django.utils.text import get_valid_filename
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from multiuploader.utils import generate_safe_pk


def _upload_to(instance, filename):
    upload_path = getattr(settings, 'MULTIUPLOADER_FILES_FOLDER', DEFAULTS.MULTIUPLOADER_FILES_FOLDER)

    if upload_path[-1] != '/':
        upload_path += '/'

    filename = get_valid_filename(os.path.basename(filename))
    filename, ext = os.path.splitext(filename)
    hash = sha1(str(time.time())).hexdigest()
    fullname = os.path.join(upload_path, "%s.%s%s" % (filename, hash, ext))

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
