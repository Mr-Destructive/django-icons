# coding=utf-8
"""
Django settings for example project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'I am a man of constant sorrow, I’ve seen trouble all of my days;'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django_icons',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tests.app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tests.app.urls'

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

WSGI_APPLICATION = 'tests.app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static URL
STATIC_URL = '/static/'


# Hack to disable migrations
# Based on: https://simpleisbetterthancomplex.com/tips/2016/08/19/django-tip-12-disabling-migrations-to-speed-up-unit-tests.html  # NOQA
class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        import django
        return None if not django.get_version().startswith('1.8') else 'notmigrations'


MIGRATION_MODULES = DisableMigrations()

# Settings for django-icons
DJANGO_ICONS = {

    'DEFAULTS': {
        'renderer': 'fontawesome',
        'attrs': {
            'aria-hidden': True
        }
    },

    'RENDERERS': {
        'fontawesome': 'FontAwesomeRenderer',
        'bootstrap3': 'Bootstrap3Renderer',
        'material': 'MaterialRenderer',
        'image': 'ImageRenderer',
    },

    'ICONS': {
        'delete': 'trash',
        'edit': {
            'name': 'pencil',
            'title': 'Edit',
        },
        'feather': {
            'renderer': 'tests.app.renderers.CustomSvgRenderer',
        },
        'paperplane': {
            'renderer': 'tests.app.renderers.CustomSvgRenderer',
        }
    },

}
