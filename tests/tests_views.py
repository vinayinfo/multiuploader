from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

import mock


class MultiuploaderViewTest(TestCase):

    @mock.patch('sorl.thumbnail.get_thumbnail')
    def test_uploading_image(self, mock_get_thumbnail):
        """Test upload single image file"""
        mock_get_thumbnail.return_value = u''
        with open(settings.TEST_DATA_DIR+'/test_image.png', 'rb') as att:
            form_data = {'file': SimpleUploadedFile(att.name, att.read())}
            resp = self.client.post('/multiuploader/', data=form_data)
            self.assertEqual(resp.status_code, 200)
            data = {u'files': [{u'thumbnailUrl': mock_get_thumbnail.return_value,
                                u'name': u'test_image.png', u'url': u'/multiuploader_file/1/',
                                u'id': u'1', u'deleteType': u'DELETE', u'type': u'text/plain',
                                u'deleteUrl': u'/multiuploader_file/1/', u'size': 180}]}
            self.assertEqual(data, resp.json())
