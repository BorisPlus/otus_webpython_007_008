from configurations import Configuration
import os
import platform

from hashlib import sha256


def get_secret_key():
    h = sha256()
    h.update(platform.node().encode())
    return h.hexdigest()


class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_secret_key())

    DEBUG = False
    ALLOWED_HOSTS = []
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'dist_learn_app',
        'manage_app',
        'user_app',
        'templates_app',

        'rest_framework',
    ]
    MIDDLEWARE = [
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ROOT_URLCONF = 'applicatura.urls'
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
    WSGI_APPLICATION = 'applicatura.wsgi.application'

    DATABASES = {
    }

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
    LANGUAGE_CODE = 'ru-ru'
    TIME_ZONE = 'Europe/Moscow'

    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.SessionAuthentication',
        )
    }

    JWT_AUTH = {
        'JWT_RESPONSE_PAYLOAD_HANDLER': 'api_ver_0_app.utils.jwt_response_handler',
    }


class BaseDev(Base):
    DEBUG = True
    INTERNAL_IPS = ('127.0.0.1', 'localhost',)  #

    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware']
    MIDDLEWARE.extend(Base.MIDDLEWARE)

    INSTALLED_APPS = Base.INSTALLED_APPS[:]
    INSTALLED_APPS.append('debug_toolbar')

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
