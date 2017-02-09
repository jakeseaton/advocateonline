"""
Django settings for advo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


ALLOWED_HOSTS = []

ADMINS = (
    ('Brendan Bozorgmir', 'technology@theharvardadvocate.com'),
    ('Nicholas Hasselmo', 'nicholashasselmo@college.harvard.edu'),
    ('Alexander Goldberg', 'alexandergoldberg@college.harvard.edu'),
    # ('Alex Sedlack', 'asedlack@college.harvard.edu'),
    ('Sammy Mehra', 'smehra@college.harvard.edu')
)

MANAGERS = ADMINS

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'tinymce',
    'ajax_select',
    'magazine',
    'blog',
    'payments',
    'django_social_share',
    'contacts',
    'redactor',
    'select2',
    'anthology',
    'rest_framework',
    'api',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'advo.urls'

WSGI_APPLICATION = 'advo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    #http://stackoverflow.com/questions/3756841/django-media-url-blank
    'django.core.context_processors.media',
    'magazine.context_processors.search_typeahead',
)

AJAX_LOOKUP_CHANNELS = {
     'contributor' : ('magazine.lookups', 'ContributorLookup'),
     'tag' : ('magazine.lookups', 'TagLookup'),
}

STRIPE_BUY_PUBLIC_KEY = os.environ.get("STRIPE_BUY_PUBLIC_KEY", "pk_test_7mkjcG8fQj3qmdhCgP92Pq4g")
STRIPE_DONATE_PUBLIC_KEY = os.environ.get("STRIPE_DONATE_PUBLIC_KEY", "pk_test_66u2FQCcD717Ot7UGj1IvEsN")

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'paste_retain_style_properties': "color font-size",
    'content_css': "/static/magazine/css/tinymce_custom.css",
    'theme': "advanced",
    'cleanup_on_startup': False,
    'custom_undo_redo_levels': 10,
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'PAGE_SIZE': 10
}

# Setting up logs
# http://ianalexandr.com/blog/getting-started-with-django-logging-in-5-minutes.html
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'WARNING',
#             'class': 'logging.FileHandler',
#             'filename': 'advocatemain.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers':['file'],
#             'propagate': True,
#             'level':'WARNING',
#         },
#         'magazine': {
#             'handlers': ['file'],
#             'level': 'WARNING',
#         },
#         'payments': {
#             'handlers': ['file'],
#             'level': 'WARNING',
#         },
#     }
# }

REDACTOR_OPTIONS = {'lang': 'en'}
REDACTOR_UPLOAD = 'uploads/'

try:
    from local_settings import *
except ImportError:
    pass

try:
    from search_settings import *
except ImportError:
    pass


import django
from django.conf import settings
from django.core.mail import send_mail
