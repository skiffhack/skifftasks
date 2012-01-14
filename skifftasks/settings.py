# -*- coding: utf-8 -*-
import os, sys, urlparse
from django.conf import global_settings

PROJECT_PATH = os.path.split(__file__)[0]
ROOT_PATH = PROJECT_PATH
sys.path.append(os.path.join(PROJECT_PATH, 'tasket', 'server'))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

SITE_URL = 'http://skifftasks.herokuapp.com'

LOGIN_REDIRECT_URL = '/'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'database', 'db.sqlite'),
    }
}

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/media/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'tasket', 'client', 'media'),
    os.path.join(PROJECT_PATH, 'client', 'media'),
)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_PATH + '/client/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/adminmedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i50qg=vmpt3)9egf1an3sau)*zp!g6#bkufd0j9lgj9brse))%'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'utils.middleware.CORSAuthorizationMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'utils.middleware.CORSMiddleware'
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH + '/templates',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django_browserid.context_processors.browserid_form',
    'django.core.context_processors.static',
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'tasks',
    'frontend',
    'sorl.thumbnail',
    'indexer',
    'paging',
    'sentry',
    'sentry.client',
    'south',
    'gunicorn',
    'django_browserid',  # Load after auth to monkey-patch it.
]

DEFAULT_TYPE = (
    'text/javascript',
    'application/javascript',
    'application/json',
    'text/html'
)

DEFAULT_HEADERS = (
    ('Access-Control-Allow-Origin', '*'),
    ('Access-Control-Allow-Headers', 'Content-Type, X-Requested-With, X-CSRFToken, Authorization, *'),
    ('Access-Control-Allow-Methods', 'POST, PUT, DELETE, GET, OPTIONS'),
    ('Access-Control-Allow-Credentials', 'true'),
)

CORS_PATHS = (
    ('/hubs/',  DEFAULT_TYPE , DEFAULT_HEADERS), 
    ('/tasks/', DEFAULT_TYPE , DEFAULT_HEADERS),
    ('/users/', DEFAULT_TYPE , DEFAULT_HEADERS),
    ('/login/', DEFAULT_TYPE , DEFAULT_HEADERS),
    ('/register/', DEFAULT_TYPE , DEFAULT_HEADERS),
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_browserid.auth.BrowserIDBackend',
)

BROWSERID_CREATE_USER = True

THUMBNAIL_DUMMY = True
INTERNAL_IPS = ('127.0.0.1',)
ADMIN_MEDIA_PREFIX
EXPOSED_SETTINGS = ("TASK_ESTIMATE_MAX", "TASK_LIMIT", "CLAIMED_LIMIT", "USERS_CAN_CREATE_HUBS", "DONE_TIME_LIMIT", "CLAIMED_TIME_LIMIT", "AUTOVERIFY_TASKS_DONE_BY_OWNER")

DEBUG = True
TEMPLATE_DEBUG = True

import logging
logger = logging.getLogger("sentry.errors")
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# From tasket's local_settings
# How many tasks a hub can have - for the Notepad app, use -1
TASK_LIMIT = 10

# How many tasks a user can claim - for the Notepad app, use -1
CLAIMED_LIMIT = 5

# Maximum task estimate
TASK_ESTIMATE_MAX = 14400

# Time limit on completing a task
CLAIMED_TIME_LIMIT = 72
DONE_TIME_LIMIT = 72

# Whether or not normal users can create hubs (admins can always create them)
USERS_CAN_CREATE_HUBS = True

# If a task is set to state "done" by its owner, then automatically verify it (see js/models/task.js)
AUTOVERIFY_TASKS_DONE_BY_OWNER = True

# Email messages from
DEFAULT_FROM_EMAIL = "Tasket Robot <tasket-robot@example.com>"

# Email routing
# EMAIL_PORT = 25
# EMAIL_HOST = "localhost"

# Turn CORS on or off (default: False)
# CROSS_DOMAIN = False

# All top-level pages that should be made accessible
INDEX_PATHS = ["tank.html", "notepad.html",]

# Uncomment the next line to change the default index files from tank.html to notepad.html
# DEFAULT_INDEX_FILE = "notepad.html"
