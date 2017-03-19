
# Multiuploader [![Build Status](https://travis-ci.org/vinaypost/multiuploader.svg?branch=master)](https://travis-ci.org/vinaypost/multiuploader) [![Build Status](https://img.shields.io/pypi/v/multiuploader.svg?style=flat)](https://pypi.python.org/pypi/djmail) [![Build Status](https://img.shields.io/pypi/dm/multiuploader.svg?style=flat)](https://pypi.python.org/pypi/djmail)

  
  
Multiuploader - is an application which enable ability to upload
multiple files in Django.

Installation
============



    $ pip install multiuploader

Then you should append 'multiuploader' to your INSTALLED\_APPS and run


    $ python manage.py makemigrations
    $ python manage.py migrate multiuploader

Also, if you want previews for uploaded images you need to do syncdb for
sorl.thumbnail.


You must have at least Django 1.10 version or later.

Also you need to append ‘multiuploader.context\_processors.booleans’ to
your ``TEMPLATE_CONTEXT_PROCESSORS``.

Setup
=====

In your settings.py you may use these options to configure application:

``MULTIUPLOADER_FILES_FOLDER`` = 'multiuploader' - media location where to store files

``MULTIUPLOADER_FILE_EXPIRATION_TIME`` = 3600 - time, when the file is expired (and it can be cleaned with clean\_files command).

``MULTIUPLOADER_FORMS_SETTINGS`` = 
:: 

    {
    'default': {
        'FILE_TYPES' : ["txt","zip","jpg","jpeg","flv","png"],
        'CONTENT_TYPES' : [
                'image/jpeg',
                'image/png',
                'application/msword',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                'application/vnd.ms-excel',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                'application/vnd.ms-powerpoint',
                'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                'application/vnd.oasis.opendocument.text',
                'application/vnd.oasis.opendocument.spreadsheet',
                'application/vnd.oasis.opendocument.presentation',
                'text/plain',
                'text/rtf',
                    ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER':5,
	'AUTO_UPLOAD': True,
    },
    'images':{
        'FILE_TYPES' : ['jpg', 'jpeg', 'png', 'gif', 'svg', 'bmp', 'tiff', 'ico' ],
        'CONTENT_TYPES' : [
            'image/gif',
            'image/jpeg',
            'image/pjpeg',
            'image/png',
            'image/svg+xml',
            'image/tiff',
            'image/vnd.microsoft.icon',
            'image/vnd.wap.wbmp',
            ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER':5,
	'AUTO_UPLOAD': True,
    },
    'video':{
        'FILE_TYPES' : ['flv', 'mpg', 'mpeg', 'mp4' ,'avi', 'mkv', 'ogg', 'wmv', 'mov', 'webm' ],
        'CONTENT_TYPES' : [
            'video/mpeg',
            'video/mp4',
            'video/ogg',
            'video/quicktime',
            'video/webm',
            'video/x-ms-wmv',
            'video/x-flv',
            ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER':5,
	'AUTO_UPLOAD': True,
    },
    'audio':{
        'FILE_TYPES' : ['mp3', 'mp4', 'ogg', 'wma', 'wax', 'wav', 'webm' ],
        'CONTENT_TYPES' : [
            'audio/basic',
            'audio/L24',
            'audio/mp4',
            'audio/mpeg',
            'audio/ogg',
            'audio/vorbis',
            'audio/x-ms-wma',
            'audio/x-ms-wax',
            'audio/vnd.rn-realaudio',
            'audio/vnd.wave',
            'audio/webm'
            ],
        'MAX_FILE_SIZE': 10485760,
        'MAX_FILE_NUMBER':5,
	'AUTO_UPLOAD': True,
    }} 
    

it is a dictionary with multiple form settings. When you append a multiuploader, you can choose a preconfigured form type, which will accept only extensions and content types you've provided.


All these parameters are optional.
