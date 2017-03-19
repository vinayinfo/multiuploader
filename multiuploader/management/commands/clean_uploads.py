from __future__ import print_function, unicode_literals

import os
from datetime import timedelta

import multiuploader.default_settings as DEFAULTS
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.timezone import now
from multiuploader.models import MultiuploaderFile


class Command(BaseCommand):
    help = 'Clean all temporary attachments loaded to MultiuploaderFile model'

    def handle(self, *args, **options):
        expiration_time = getattr(settings, "MULTIUPLOADER_FILE_EXPIRATION_TIME",
                                  DEFAULTS.MULTIUPLOADER_FILE_EXPIRATION_TIME)
        time_threshold = now() - timedelta(seconds=expiration_time)

        for attach in MultiuploaderFile.objects.filter(upload_date__lt=time_threshold):
            try:
                os.remove(attach.file.path)
            except Exception as ex:
                print(ex)

        MultiuploaderFile.objects.filter(upload_date__lt=time_threshold).delete()

        print("Cleaning temporary upload files complete")
