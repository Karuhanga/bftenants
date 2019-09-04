import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url

from chalicelib.config import get_secret

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4s%9xjc7+%ubr98s!zf$en1qi@=8_tpdf3tfoog_g&ogv2)lu#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'chalicelib.data.models',
]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default=get_secret('DATABASE_URL') if os.environ.get('DEBUG', 'True') == 'False' else os.environ.get('DATABASE_URL', 'postgres://bftenantsuser:1234@localhost/bftenants')
    )
}


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
