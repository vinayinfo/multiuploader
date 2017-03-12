# -*- encoding: utf-8 -*-

SECRET_KEY = 'p23jof024jf5-94j3f023jf230=fj234fp34fijo'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
    }
}

INSTALLED_APPS = [
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

CELERY_TASK_ALWAYS_EAGER = True
