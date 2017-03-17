from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http.response import JsonResponse
from django.test import TestCase

import mock


class MultiuploaderViewTest(TestCase):
    """Test uploading functionality"""
    @mock.patch('sorl.thumbnail.get_thumbnail')
    def test_uploading_image(self, mock_get_thumbnail):
        """Test upload single image file"""
        mock_get_thumbnail.return_value = ""
        with open(settings.TEST_DATA_DIR+'/test.png', 'rb') as att:
            form_data = {'file': SimpleUploadedFile(att.name, att.read()), 'media_type': 'images'}
            resp = self.client.post('/multiuploader/', data=form_data)
            self.assertEqual(resp.status_code, 200)
            data = {"files": [{"id": "1",
                          "name": "test.png",
                          "size": 180,
                          'type': "text/plain",
                          "url": "/multiuploader_file/1/",
                          "thumbnailUrl": "",
                          "deleteUrl": "/multiuploader_file/1/",
                          "deleteType": "DELETE", }]
               }
            self.assertEqual(resp.content, JsonResponse(data).content)
            resp = self.client.get('/multiuploader_file/1/', HTTP_USER_AGENT='Mozilla/5.0')
            self.assertEqual(resp.status_code, 200)
            resp = self.client.delete('/multiuploader_file/1/')
            self.assertEqual(resp.status_code, 200)

    @mock.patch('sorl.thumbnail.get_thumbnail')
    def test_uploading_mp3(self, mock_get_thumbnail):
        """Test upload single mp3 file"""
        mock_get_thumbnail.return_value = ""
        with open(settings.TEST_DATA_DIR + '/test.mp3', 'rb') as att:
            form_data = {'file': SimpleUploadedFile(att.name, att.read()), 'media_type': 'audio'}
            resp = self.client.post('/multiuploader/', data=form_data)
            self.assertEqual(resp.status_code, 200)
            data = {"files": [{"id": "2",
                               "name": "test.mp3",
                               "size": 3742720,
                               'type': "text/plain",
                               "url": "/multiuploader_file/2/",
                               "thumbnailUrl": "",
                               "deleteUrl": "/multiuploader_file/2/",
                               "deleteType": "DELETE", }]
                    }
            self.assertEqual(resp.content, JsonResponse(data).content)
            resp = self.client.get('/multiuploader_file/2/', HTTP_USER_AGENT='Mozilla/5.0')
            self.assertEqual(resp.status_code, 200)
            resp = self.client.delete('/multiuploader_file/2/')
            self.assertEqual(resp.status_code, 200)

    @mock.patch('sorl.thumbnail.get_thumbnail')
    def test_uploading_pdf(self, mock_get_thumbnail):
        """Test upload single pdf file"""
        mock_get_thumbnail.return_value = ""
        with open(settings.TEST_DATA_DIR + '/test.pdf', 'rb') as att:
            form_data = {'file': SimpleUploadedFile(att.name, att.read()), 'media_type': 'default'}
            resp = self.client.post('/multiuploader/', data=form_data)
            self.assertEqual(resp.status_code, 200)
            data = {"files": [{"id": "3",
                               "name": "test.pdf",
                               "size": 6763,
                               'type': "text/plain",
                               "url": "/multiuploader_file/3/",
                               "thumbnailUrl": "",
                               "deleteUrl": "/multiuploader_file/3/",
                               "deleteType": "DELETE", }]
                    }
            self.assertEqual(resp.content, JsonResponse(data).content)
            resp = self.client.get('/multiuploader_file/3/', HTTP_USER_AGENT='Mozilla/5.0')
            self.assertEqual(resp.status_code, 200)
            resp = self.client.delete('/multiuploader_file/3/')
            self.assertEqual(resp.status_code, 200)