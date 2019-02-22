import os
from celery.schedules import crontab


USE_LOADING_SCREEN = os.environ.get('USE_LOADING_SCREEN', False)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '8@jl6lay-4-xzjdic2#mw%e2c@%*o1nfh&k@95p2=&x%5n&n@g'

DEBUG = True

ALLOWED_HOSTS = ['192.168.0.108', 'localhost', 'redis://localhost']

INSTALLED_APPS = [
    'website',
    'dashboard',
    's3direct',
    'tinymce',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
]

CSRF_FAILURE_VIEW = 'website.views.home'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'theearthissquare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['dashboard/templates'],
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

WSGI_APPLICATION = 'theearthissquare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'website/static'),
    os.path.join(BASE_DIR, 'dashboard/static'),
)

ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'hello@theearthissquare.com')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = True
EMAIL_PORT = 587

LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

FACEBOOK_GRAPH_API_ACCESS_KEY = os.environ.get('FACEBOOK_GRAPH_API_ACCESS_KEY', 'EAAXyjkCQvyIBANoVZB5dKa9hLyxIz34SKWP2CiwNiutFgEeusBjMvAH1vaIr6wMdk9KOLZCfupSoi0YxmFJVR0H1lOPHEWpRi6q9lUMN5vDuNwJzZCNZCXHgeM2dTInB6b1vZCF9lEyQK6pAet8woCsBmZBdSMEu0ZD')

# Celery application definition
# http://docs.celeryproject.org/en/v4.0.2/userguide/configuration.html
CELERY_BROKER_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Australia/Melbourne'
CELERY_BEAT_SCHEDULE = {
    'task_updateDashboard': {
        'task': 'dashboard.tasks.task_updateDashboard',
        'schedule': crontab(minute='*/10'),
    },
    'task_createStatsLog': {
        'task': 'dashboard.tasks.task_createStatsLog',
        'schedule': crontab(minute=0, hour='*/3'),
    }
}
