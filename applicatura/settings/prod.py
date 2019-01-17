from . import base

import os


class Prod(base.Base):
    ALLOWED_HOSTS = ['*']

    SECRET_KEY = ''

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(base.Base.BASE_DIR, 'db.prod.sqlite3'),
        }
    }
