"""
Django settings for ArgusWatcher project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from environ import Env

env = Env(
    DEBUG=(bool, False)  # default value
)

# path of django proejct folder
BASE_DIR = Path(__file__).resolve().parent.parent

# read the env file from the base dir
env.read_env(Path(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap5',
    'AppEC2',
    'AppShowcase',
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

ROOT_URLCONF = 'ArgusWatcher.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'ArgusWatcher.wsgi.application'


# Database
DATABASES = {
    # overrides the default db
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env("MYSQL_DB_NAME"),
        'USER': env("MYSQL_USERNAME"),
        'PASSWORD': env("MYSQL_PASSWORD"),
        'HOST': env("MYSQL_HOST"),
        'PORT': env("MYSQL_PORT"),
        'OPTIONS': {
            # used to handle the invalid or missing values from being stored in the database by INSERT and UPDATE statements.
            # STRICT_TRANS_TABLES mode: If a value could not be inserted as given into a transactional table, abort the statement.
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = 'static'  # collectstatic


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# the path of private key .pem file to connect instance with ssh
RSAKEY_PATH = Path(BASE_DIR, "RSAKey.pem")

# reserved for later version
# Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = env("EMAIL_HOST")  # looking up the value EMAIL_HOST
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

# # a custom setting to send the emails to an address can be accessed.
# RECIPIENT_ADDRESS = env('RECIPIENT_ADDRESS')
