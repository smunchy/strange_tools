# Django settings for newproject project.
import os

# This sets the variable project root, to be the dir name, path to the dir, that contains the settings file.

PROJECT_ROOT = os.path.dirname(__file__)

# python manage.py test runs over all django/python tests

# Set to Debug mode, instead of prod mode.
DEBUG = True
# Sets to same as debug variable
TEMPLATE_DEBUG = DEBUG

# tuples are used with parenthesis, they are immutable.
# Handy for things that dont change.
# If problem with site, it will email you.
ADMINS = (
    ('Sean Fallon', 'seanfallon.web@gmail.com'),
    ('Aaron Neuhauser', 'aaronneuhauser@yahoo.com'),
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# example of dictionary
# can set more than one DB
# Make sure pathing is right on 'NAME' in order to syncdb

# Sean's NAME:'///home/sean/newproject/testdb.db'
# Aaron's NAME:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '///home/sean/newproject/testdb.db' #% PROJECT_ROOT,                      # Or path to database file if using sqlite3.
        #'USER': '',                      # Not used with sqlite3.
        #'PASSWORD':' ',                  # Not used with sqlite3.
        #'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        #'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# This shows multiple sites.
# You will have multiple setting files for django, setting site id for each one.
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# tells django where our media is going to live.
# Media root is what python of django uses if you have an uploaded file.
# or storing an image.
MEDIA_ROOT = '%s/../public/media/' % PROJECT_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
# MEDIA URl is what you use in your templates.
#
MEDIA_URL = 'http://cipetools.epictools.dev'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'k8&r(5*3(f!m4yiew5-dfz4e1dln7a_^u-2tnm_b@&#wdw0#vo'

# List of callables that know how to import templates from various sources.
# Functions or classes that call on where to find templates
# uncomment last line for eggs.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

# REquest comes in and makes it to where django is.
# Django sends it through it order.
# processes it in views.
# then sends it through middleware and back out.
# Allows you to pass messages to users for authentication.
# Modify sessions, etc.
# make own middleware and can add it here.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# delete up to urls, so it can recognize multiple sites
ROOT_URLCONF = 'urls'

# Templates all in one folder
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT,'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# apps that are turned on
# allows us to create users
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',

    # My apps
    'epictools',

    # third party apps
    'south', # must syncdb after adding south
    'taggit',

    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# This tries to find a file, relative to this dir
# if it finds it, it imports everything from this file
try:
    from local_settings import *

except ImportError:
    pass

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

##### Git Documentation #####

# Django taggit or other apps from github
# sudo pip install -e git+http://github.com/the/rest/of/the/link/goes/here/lol.git#egg=whatever_namehere
# this will our virtual environment ( virtualenv ) install django taggit installed inside of a container called django tagit
