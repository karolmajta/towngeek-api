"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import os
import ConfigParser

from django.conf import ImproperlyConfigured

project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
config_path = os.path.join(project_root, 'towngeek.cfg')
config = ConfigParser.ConfigParser()
try:
    with open(config_path, 'r') as fp:
        config.readfp(fp)
except IOError:
    msg = u"`towngeek.cfg` is missing in git checkouts root folder." \
         + "Please consult README.md."
    raise ImproperlyConfigured(msg)

# some cleanup and sanity checking for what is set in the cfg file
try:
    file_config = {
        'debug': config.getboolean("django:debug", "debug"),
        'default_db_engine': config.get("django:databases", "default-database-engine"),
        'default_db_name': config.get("django:databases", "default-database-name"),
        'default_db_user': config.get("django:databases", "default-database-user"),
        'default_db_password': config.get("django:databases", "default-database-password"),
        'default_db_host': config.get("django:databases", "default-database-host"),
        'default_db_port': config.get("django:databases", "default-database-port"),

        'allowed_hosts': config.get("django:server", "allowed-hosts") \
                               .replace(" ", "") \
                               .split(","),
        'server_secret': config.get("django:server", "server-secret"),

        'broker_url': config.get("django:queue", "broker-url"),

        'timezone': config.get("django:locale", "timezone"),
        'language_code': config.get("django:locale", "language-code"),

        'email_host': config.get("django:email", "email-host"),
        'email_port': config.get("django:email", "email-port"),
        'email_user': config.get("django:email", "email-user"),
        'email_password': config.get("django:email", "email-password"),

        'tg_reply_to': config.get("towngeek:mailing", "reply-to"),
    }
except ConfigParser.NoOptionError as e:
    msg = u"Missing option `{0}` in section `{1}` in configuration file."
    raise ImproperlyConfigured(msg.format(e.option, e.section))
except ConfigParser.NoSectionError as e:
    msg = u"Mission section `{0}` in configuration file."
    raise ImproperlyConfigured(msg.format(e.section))

###############################################################################

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import djcelery
djcelery.setup_loader()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y%-x=*l%!cxt6apza48j@=e))g80&mvmefy+)tvgftg9#@%gmq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = file_config['debug']

TEMPLATE_DEBUG = file_config['debug']

ALLOWED_HOSTS = file_config['allowed_hosts']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',
    'rest_framework',
    'rest_framework.authtoken',
    'djcelery',

    'towngeek.commons',
    'towngeek.locations',
    'towngeek.qa',
    'towngeek.ratings',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + file_config['default_db_engine'],
        'NAME': file_config['default_db_name'],
        # The following settings are not used with sqlite3:
        'USER': file_config['default_db_user'],
        'PASSWORD': file_config['default_db_password'],
        'HOST': file_config['default_db_host'],
        'PORT': file_config['default_db_port'],
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = file_config['language_code']

TIME_ZONE = file_config['timezone']

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = file_config['email_host']
EMAIL_PORT = file_config['email_port']
EMAIL_HOST_USER = file_config['email_user']
EMAIL_HOST_PASSWORD = file_config['email_password']

# project templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# Celery
BROKER_URL = file_config['broker_url']

# Towngeek specific settings. Use `towngeek.commons.conf.settings`
# to access them in convenient way.
TOWNGEEK = {
    'REPLY_TO': file_config['tg_reply_to'],
}