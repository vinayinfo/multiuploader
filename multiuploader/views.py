from __future__ import unicode_literals

import json
import logging

from django.core.files.uploadedfile import UploadedFile
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormView
from multiuploader.forms import MultiUploadForm
from multiuploader.models import MultiuploaderFile
from multiuploader.utils import FileResponse
from sorl.thumbnail import get_thumbnail

try:
    from django.urls import reverse
except ImportError as ie:
    from django.core.urlresolvers import reverse

log = logging


class MultiuploaderView(FormView):
    """
    This class will add use for uploading files.
    """
    form_class = MultiUploadForm
    model = MultiuploaderFile

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        """
        log.info('received POST to main multiuploader view')
        file_obj = self.request.FILES['file']
        wrapped_file = UploadedFile(file_obj)
        filename = wrapped_file.name
        file_size = wrapped_file.file.size
        log.info('Got file: "%s"' % filename)
        fl = self.model()
        fl.filename = filename
        fl.file = file_obj
        fl.save()
        log.info('File saving done')
        thumb_url = ""
        size = self.request.GET.get('size')
        size = size if size else '180x80'
        quality = self.request.GET.get('quality')
        quality = quality if quality else 50
        try:
            im = get_thumbnail(fl.file, size, quality=quality)
            thumb_url = im.url
        except Exception as e:
            log.error(e)
        # generating json response array
        result = {"files": [{"id": str(fl.id),
                             "name": filename,
                             "size": file_size,
                             'type': file_obj.content_type,
                             "url": reverse('multiuploader', args=[fl.pk]),
                             "thumbnailUrl": thumb_url,
                             "deleteUrl": reverse('multiuploader', args=[fl.pk]),
                             "deleteType": "DELETE", }]
                  }

        return JsonResponse(result)

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        """
        error = _("Unknown error")
        if "file" in form._errors and len(form._errors["file"]) > 0:
            error = form._errors["file"][0]

        response_data = [{"error": error}]
        return HttpResponse(json.dumps(response_data))

    def get(self, request, *args, **kwarg):
        fl = get_object_or_404(MultiuploaderFile, id=kwarg.get('pk'))
        return FileResponse(request, fl.file.path, fl.filename)

    def delete(self, request, *args, **kwargs):
        """
        Calls the delete() method on the fetched object and then
        redirects to the success URL.
        """
        log.info('Called delete file. File id=' + str(kwargs.get('pk')))
        fl = get_object_or_404(MultiuploaderFile, pk=kwargs.get('pk'))
        fl.delete()
        log.info('DONE. Deleted file id=' + str(kwargs.get('pk')))

        return HttpResponse(1)
