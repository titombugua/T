"""
Django settings for T project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from dj_database_url import parse as dburl
import psycopg2




# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config('SECRET_KEY')
# SECRET_KEY = os.environ['SECRET_KEY']

SECRET_KEY = '%+6&1@&e2e$_q&4t=jms@5wb)vge0)xk$jdg_gf#%su3@j1d9@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'web.apps.WebConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django_markdown',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'julzmbugua@gmail.com'
EMAIL_HOST_PASSWORD = 'hecalledmeintelligentcoward'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

ROOT_URLCONF = 'T.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['web/templates/web'],
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

WSGI_APPLICATION = 'T.wsgi.application'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
                ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
                 'JustifyRight', 'JustifyBlock', 'Blockquote'],
                ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Format", "Subscript", "Superscript", "PageBreak"], ['Undo', 'Redo'], ["Source"],
                ["Maximize"]],
        
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 't_web',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    }
}
# THE MAGIC CODE THAT HAS ENABLED ME TO RUN POSTGRES LOCAL AND REMOTE(DIFFERENT DATABASES)
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)




# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd25ck31jvd4p8m',
#         'USER': 'prtjluvdnhsanj',
#         'PASSWORD': 'c6d93658711194e815a70abe33fa912978508ec16550b89b6f7285e76906e9fc',
#         'HOST': 'ec2-23-21-204-166.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dubai'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# ckeditor



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

CKEDITOR_UPLOAD_PATH = "uploads/"

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"), 
#     'media',

STATIC_ROOT = 'web/static/'
MEDIA_URL = '/'
MEDIA_ROOT = 'web/media/'
