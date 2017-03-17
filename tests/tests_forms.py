from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from multiuploader.forms import MultiUploadForm


class MultiUploadFormValidationTest(TestCase):
    """Test MultiUploadForm form validation"""
    def test_forms(self):
        with open(settings.TEST_DATA_DIR+'/test.png', 'rb') as att:
            form_data = {}
            form = MultiUploadForm(data=form_data, files={'file': SimpleUploadedFile(att.name, att.read())})
            self.assertTrue(form.is_valid())
