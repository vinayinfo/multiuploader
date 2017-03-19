from __future__ import unicode_literals

import logging
import mimetypes
import os
from wsgiref.util import FileWrapper

from django.conf import settings
from django.http import HttpResponse

try:
    from urllib import quote
except ImportError as ie:
    from urllib.parse import quote



log = logging


# Getting files here
def format_file_extensions(extensions):
    return ".(%s)$" % "|".join(extensions)


class FileResponse(HttpResponse):
    def __init__(self, request, filepath, filename=None, status=None):

        if settings.DEBUG:
            wrapper = FileWrapper(file(filepath, 'rb'))
            super(FileResponse, self).__init__(wrapper, status=status)
        else:
            super(FileResponse, self).__init__(status=status)
            self['X-Accel-Redirect'] = filepath
            self['XSendfile'] = filepath

        if not filename:
            filename = os.path.basename(filepath)

        type, encoding = mimetypes.guess_type(filepath)

        if type is None:
            type = 'application/octet-stream'

        self['Content-Type'] = type
        self['Content-Length'] = os.path.getsize(filepath)

        if encoding is not None:
            self['Content-Encoding'] = encoding

        # To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
        if u'WebKit' in request.META['HTTP_USER_AGENT']:
            # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
            filename_header = 'filename={}'.format(filename.encode('utf-8'))
        elif u'MSIE' in request.META['HTTP_USER_AGENT']:
            # IE does not support internationalized filename at all.
            # It can only recognize internationalized URL, so we do the trick via routing rules.
            filename_header = ''
        else:
            # For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
            filename_header = 'filename*=UTF-8\'\'{}'.format(quote(filename.encode('utf-8')))

        self['Content-Disposition'] = 'attachment; ' + filename_header
