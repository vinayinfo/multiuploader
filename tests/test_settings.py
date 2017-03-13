# -*- encoding: utf-8 -*-
import os

SECRET_KEY = 'p23jof024jf5-94j3f023jf230=fj234fp34fijo'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_DATA_DIR = os.path.join(BASE_DIR, 'tests', 'test_data')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
    }
}

INSTALLED_APPS = [
    'sorl.thumbnail',
    'tests',
    'multiuploader',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = ()

CELERY_TASK_ALWAYS_EAGER = True

ROOT_URLCONF = 'multiuploader.urls'
