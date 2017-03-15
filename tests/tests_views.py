from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http.response import JsonResponse
from django.test import TestCase

import mock


class MultiuploaderViewTest(TestCase):

    @mock.patch('sorl.thumbnail.get_thumbnail')
    def test_uploading_image(self, mock_get_thumbnail):
        """Test upload single image file"""
        mock_get_thumbnail.return_value = ""
        with open(settings.TEST_DATA_DIR+'/test_image.png', 'rb') as att:
            form_data = {'file': SimpleUploadedFile(att.name, att.read())}
            resp = self.client.post('/multiuploader/', data=form_data)
            self.assertEqual(resp.status_code, 200)
            data = {"files": [{"id": "1",
                          "name": "test_image.png",
                          "size": 180,
                          'type': "text/plain",
                          "url": "/multiuploader_file/1/",
                          "thumbnailUrl": "",
                          "deleteUrl": "/multiuploader_file/1/",
                          "deleteType": "DELETE", }]
               }
            self.assertEqual(resp.content, JsonResponse(data).content)
