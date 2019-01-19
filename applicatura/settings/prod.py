from . import base

import os


class Config(base.Base):
    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(base.Base.BASE_DIR, 'db.prod.sqlite3'),
        }
    }
